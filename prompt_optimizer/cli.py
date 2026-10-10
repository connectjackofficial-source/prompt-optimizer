"""prompt-optimizer CLI."""
import argparse
import json

from .analyzer import analyze, optimize, score


def main():
    ap = argparse.ArgumentParser(prog="prompt-optimizer")
    ap.add_argument("prompt", nargs="?", help="prompt text to analyze")
    ap.add_argument("--json", action="store_true",
                    help="machine-readable report with severity and score")
    args = ap.parse_args()
    if not args.prompt:
        ap.print_help()
        return
    if args.json:
        items = analyze(args.prompt)
        print(json.dumps({
            "score": score(args.prompt),
            "suggestions": [
                {"rule": s.rule, "severity": s.severity, "message": s.message}
                for s in items
            ],
        }, indent=2, ensure_ascii=False))
    else:
        print(f"score: {score(args.prompt)}/100")
        print(optimize(args.prompt))


if __name__ == "__main__":
    main()
