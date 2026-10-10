# prompt-optimizer

> Analyze your prompt and suggest improvements: missing role, no examples,
> vague words, too long, too short.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

## Usage

```python
from prompt_optimizer.analyzer import optimize

print(optimize("write something good"))
# Found 4 suggestions:
#   - [too-short] ...
#   - [no-role] ...
```

## Checks

- too short / too long
- no role specified
- no examples
- no output format
- vague words (some, maybe, good, ...)
- repeated phrases (same word 3+ times)
- contradictory constraints ("short" + "detailed")

## Programmatic API

```python
from prompt_optimizer.analyzer import analyze, repeated_phrases, has_contradictions

suggestions = analyze(prompt)   # list of Suggestion(rule, message, severity)
print(repeated_phrases(prompt)) # words used 3+ times
print(has_contradictions(prompt))  # bool
```

## Health score

Each suggestion carries a severity (`critical` / `warning` / `info`);
`score()` converts the list into a 0-100 health score:

```python
from prompt_optimizer.analyzer import score

print(score(prompt))  # 100 = nothing to fix, lower = more to improve
```

CLI reports the score and, with `--json`, a machine-readable breakdown:

```bash
python -m prompt_optimizer.cli "write stuff" --json
# {"score": 66, "suggestions": [{"rule": "no-role", "severity": "warning", ...}]}
```

## License

MIT
