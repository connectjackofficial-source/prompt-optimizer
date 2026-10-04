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

    vague = ["some", "maybe", "good", "nice", "appropriate"]
    found = [w for w in vague if w in prompt.lower()]
    if found:
        suggestions.append(Suggestion("vague-words",
            f"Vague words found: {', '.join(found)}. Be specific."))

    return suggestions


def optimize(prompt: str) -> str:
    """Return a human-readable report."""
    items = analyze(prompt)
    if not items:
        return "Prompt looks good."
    lines = [f"Found {len(items)} suggestion(s):"]
    for s in items:
        lines.append(f"  - [{s.rule}] {s.message}")
    return "\n".join(lines)
