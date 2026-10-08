"""prompt-optimizer: analyze a prompt and suggest improvements."""
from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class Suggestion:
    rule: str
    message: str


def analyze(prompt: str) -> list[Suggestion]:
    suggestions = []

    words = len(prompt.split())
    if words < 5:
        suggestions.append(Suggestion("too-short",
            "Prompt is very short. Add context about what you want."))
    if words > 500:
        suggestions.append(Suggestion("too-long",
            "Prompt is long. Consider splitting or trimming unnecessary context."))

    if "you are" not in prompt.lower() and "act as" not in prompt.lower():
        suggestions.append(Suggestion("no-role",
            "No role specified. Try 'You are a ...' to set the persona."))

    if "example" not in prompt.lower() and "for example" not in prompt.lower():
        suggestions.append(Suggestion("no-example",
            "No examples provided. Add 1-2 few-shot examples for better output."))

    if len(re.findall(r"[?？]", prompt)) > 0 and "answer" not in prompt.lower():
        suggestions.append(Suggestion("no-format",
            "Questions present but no output format specified."))

    if re.search(r"\d+\s*steps?", prompt.lower()) and \
       "step 1" not in prompt.lower() and "first" not in prompt.lower():
        suggestions.append(Suggestion("no-steps",
            "Mentions steps but does not enumerate them. Use numbered steps."))

    vague = ["some", "maybe", "good", "nice", "appropriate", "quick",
             "better", "stuff"]
    found = [w for w in vague if w in prompt.lower()]
    if found:
        suggestions.append(Suggestion("vague-words",
            f"Vague words found: {', '.join(found)}. Be specific."))

    repeat = repeated_phrases(prompt)
    if repeat:
        suggestions.append(Suggestion("repetition",
            f"Repeated phrases ({len(repeat)}): {', '.join(repeat[:3])}. "
            "Consolidate to shorten the prompt."))

    if has_contradictions(prompt):
        suggestions.append(Suggestion("contradiction",
            "Prompt contains contradictory constraints (e.g. both 'short' "
            "and 'detailed'). Pick one."))

    return suggestions


def repeated_phrases(prompt: str, min_len: int = 5, top_n: int = 5) -> list:
    """Find words repeated 3+ times as possible filler/repetition."""
    words = [w.lower() for w in re.findall(r"[a-z]+", prompt)]
    from collections import Counter
    counts = Counter(words)
    return [w for w, c in counts.most_common(top_n) if c >= 3]


def has_contradictions(prompt: str) -> bool:
    """Detect classic contradictory constraint pairs."""
    pairs = [
        ("short", "detailed"),
        ("concise", "elaborate"),
        ("brief", "thorough"),
        ("simple", "advanced"),
    ]
    low = prompt.lower()
    return any(a in low and b in low for a, b in pairs)


def optimize(prompt: str) -> str:
    """Return a human-readable report."""
    items = analyze(prompt)
    if not items:
        return "Prompt looks good."
    lines = [f"Found {len(items)} suggestion(s):"]
    for s in items:
        lines.append(f"  - [{s.rule}] {s.message}")
    return "\n".join(lines)
