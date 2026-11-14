"""Tests that take both outcomes of each decision in the Lab 6 module."""

from spam_scoring import classify, filter_inbox, inbox_status, score_message


def test_score_message_word_branches():
    # Spam term, uppercase bonus, and ordinary-word paths through the loop.
    assert score_message("FREE!", False, 0) == 2
    assert score_message("ALERT", False, 0) == 1
    assert score_message("hello", False, 0) == 0


def test_score_message_link_branches():
    assert score_message("hello", False, 4) == 4
    assert score_message("hello", False, 1) == 1
    assert score_message("hello", False, 0) == 0


def test_score_message_sender_and_floor_branches():
    # Known sender false; true with a negative intermediate score; true with
    # a nonnegative intermediate score.
    assert score_message("FREE", False, 0) == 2
    assert score_message("hello", True, 0) == 0
    assert score_message("FREE WINNER", True, 0) == 1


def test_classify_all_decision_outcomes():
    assert classify(8) == "spam"
    assert classify(4) == "suspicious"
    assert classify(0) == "clean"


def test_filter_inbox_loop_with_items_and_no_items():
    assert filter_inbox([
        ("FREE WINNER", False, 4),
        ("FREE", False, 4),
        ("hello", False, 0),
    ]) == {"spam": 1, "suspicious": 1, "clean": 1}
    assert filter_inbox([]) == {"spam": 0, "suspicious": 0, "clean": 0}


def test_inbox_status_all_ratio_decisions():
    assert inbox_status({"spam": 0, "suspicious": 0, "clean": 0}) == "empty"
    assert inbox_status({"spam": 3, "suspicious": 1, "clean": 1}) == "flooded"
    assert inbox_status({"spam": 2, "suspicious": 1, "clean": 2}) == "noisy"
    assert inbox_status({"spam": 1, "suspicious": 0, "clean": 4}) == "healthy"
