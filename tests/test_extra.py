"""Tests for repetition and contradiction detection."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from prompt_optimizer.analyzer import (has_contradictions, optimize,
                                       repeated_phrases)


def test_repeated_phrases():
    rep = repeated_phrases("the the the quick brown fox jumps the dog")
    assert "the" in rep
    assert repeated_phrases("a unique one-off sentence here") == []
    print("test_repeated_phrases: ok")


def test_has_contradictions():
    assert has_contradictions("keep it short but very detailed")
    assert not has_contradictions("write a short answer")
    print("test_has_contradictions: ok")


def test_optimize_reports_rules():
    report = optimize("the the the the the make a report about stuff")
    assert "repetition" in report
    assert "vague-words" in report
    print("test_optimize_reports_rules: ok")


if __name__ == "__main__":
    test_repeated_phrases()
    test_has_contradictions()
    test_optimize_reports_rules()
    print("prompt-optimizer extra tests passed")
