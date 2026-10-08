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

suggestions = analyze(prompt)   # list of Suggestion(rule, message)
print(repeated_phrases(prompt)) # words used 3+ times
print(has_contradictions(prompt))  # bool
```

## License

MIT
