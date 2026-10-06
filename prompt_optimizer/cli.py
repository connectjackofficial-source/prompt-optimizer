"""prompt-optimizer CLI."""
import argparse

from .analyzer import optimize


def main():
    ap = argparse.ArgumentParser(prog="prompt-optimizer")
    ap.add_argument("prompt", nargs="?", help="prompt text to analyze")
    args = ap.parse_args()
    if args.prompt:
        print(optimize(args.prompt))


if __name__ == "__main__":
    main()
