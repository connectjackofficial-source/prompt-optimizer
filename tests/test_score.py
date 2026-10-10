"""Tests for severity and scoring."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from prompt_optimizer.analyzer import analyze, score


def test_severity_assigned():
    items = analyze("write something good and keep it short but very detailed")
    rules = {s.rule for s in items}
    sev = {s.rule: s.severity for s in items}
    assert "vague-words" in rules
    assert sev.get("vague-words") == "warning"
    assert "contradiction" in rules
    assert sev.get("contradiction") == "critical"
    print("test_severity_assigned: ok")


def test_score_perfect():
    good = ("You are a senior Python engineer. Refactor the module below. "
            "Example input: x. Expected: y. Keep it concise. Do not use "
            "any vague terms or repeat yourself, follow steps 1 to 3.")
    assert score(good) >= 90
    print("test_score_perfect: ok")


def test_score_penalized():
    bad = "do stuff"
    assert score(bad) < score("You are a senior engineer. Write tests for this code.")
    assert 0 <= score(bad) <= 100
    print("test_score_penalized: ok")


if __name__ == "__main__":
    test_severity_assigned()
    test_score_perfect()
    test_score_penalized()
    print("prompt-optimizer scoring tests passed")
