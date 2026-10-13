"""Tests for auto-fix of contradictory constraints."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from prompt_optimizer.analyzer import auto_fix, has_contradictions


def test_auto_fix_removes_conflict():
    prompt = "Write a short but detailed explanation of caching"
    fixed, changes = auto_fix(prompt)
    assert changes  # at least one edit
    assert "detailed" not in fixed
    assert "short" in fixed
    assert not has_contradictions(fixed)
    print("test_auto_fix_removes_conflict: ok")


def test_auto_fix_clean_prompt():
    prompt = "Write a concise summary of caching"
    fixed, changes = auto_fix(prompt)
    assert changes == []
    assert fixed == prompt
    print("test_auto_fix_clean_prompt: ok")


def test_auto_fix_multiple_pairs():
    prompt = "Keep it simple but advanced, short and detailed"
    fixed, changes = auto_fix(prompt)
    assert any("advanced" in c for c in changes)
    assert any("detailed" in c for c in changes)
    assert "advanced" not in fixed
    assert "detailed" not in fixed
    print("test_auto_fix_multiple_pairs: ok")


if __name__ == "__main__":
    test_auto_fix_removes_conflict()
    test_auto_fix_clean_prompt()
    test_auto_fix_multiple_pairs()
    print("prompt-optimizer auto-fix tests passed")
