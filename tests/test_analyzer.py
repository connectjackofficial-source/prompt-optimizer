"""Tests for prompt-optimizer."""
from prompt_optimizer.analyzer import analyze


def test_good_prompt_clean():
    good = ("You are a code reviewer. Review this diff and list issues "
            "with examples.")
    assert analyze(good) == []
    print("test_good_prompt_clean: ok")


def test_vague_detected():
    items = analyze("write something good")
    rules = {s.rule for s in items}
    assert "vague-words" in rules
    assert "too-short" in rules
    print("test_vague_detected: ok")


def test_no_steps_detected():
    items = analyze("Give me 3 steps to deploy")
    rules = {s.rule for s in items}
    assert "no-steps" in rules
    print("test_no_steps_detected: ok")


if __name__ == "__main__":
    test_good_prompt_clean()
    test_vague_detected()
    test_no_steps_detected()
    print("prompt-optimizer tests passed")
