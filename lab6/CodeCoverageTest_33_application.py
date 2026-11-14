"""Tests focused on executing every line in the Lab 6 spam scorer."""

from spam_scoring import classify, filter_inbox, inbox_status, score_message


def test_plain_message_scores_zero():
    assert score_message("hello there", False, 0) == 0


def test_spam_words_are_case_insensitive_and_strip_punctuation():
    assert score_message("FREE! winner, Prize.", False, 0) == 6


def test_long_uppercase_words_add_one_point():
    assert score_message("HELLO WORLD", False, 0) == 2


def test_short_uppercase_words_do_not_add_points():
    assert score_message("OK YES", False, 0) == 0


def test_link_count_over_three_adds_four_points():
    assert score_message("hello", False, 4) == 4


def test_one_to_three_links_add_one_point():
    assert score_message("hello", False, 2) == 1


def test_known_sender_reduces_score_without_going_below_zero():
    assert score_message("FREE", True, 0) == 0


def test_known_sender_reduces_a_positive_score():
    assert score_message("FREE WINNER", True, 0) == 1


def test_classification_for_each_label():
    assert classify(8) == "spam"
    assert classify(4) == "suspicious"
    assert classify(3) == "clean"


def test_filter_inbox_counts_each_class():
    messages = [
        ("FREE WINNER", False, 4),
        ("FREE", False, 4),
        ("hello", False, 0),
    ]
    assert filter_inbox(messages) == {"spam": 1, "suspicious": 1, "clean": 1}


def test_filter_empty_inbox():
    assert filter_inbox([]) == {"spam": 0, "suspicious": 0, "clean": 0}


def test_inbox_status_for_empty_flooded_noisy_and_healthy():
    assert inbox_status({"spam": 0, "suspicious": 0, "clean": 0}) == "empty"
    assert inbox_status({"spam": 3, "suspicious": 1, "clean": 1}) == "flooded"
    assert inbox_status({"spam": 2, "suspicious": 1, "clean": 2}) == "noisy"
    assert inbox_status({"spam": 1, "suspicious": 0, "clean": 4}) == "healthy"
