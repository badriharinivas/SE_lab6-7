from hypothesis import settings
from hypothesis import given, strategies as st
from spam_scoring import sender_domain, first_link, shout_ratio


FUZZ_SETTINGS = settings(max_examples=100, derandomize=True)


@FUZZ_SETTINGS
@given(st.one_of(st.text(), st.none()))
def test_sender_domain_handles_arbitrary_input(value):
    result = sender_domain(value)
    assert isinstance(result, str)


@FUZZ_SETTINGS
@given(st.one_of(st.text(), st.none()))
def test_first_link_handles_arbitrary_input(value):
    result = first_link(value)
    assert isinstance(result, str)


@FUZZ_SETTINGS
@given(st.one_of(st.text(), st.none()))
def test_shout_ratio_handles_arbitrary_input(value):
    result = shout_ratio(value)
    assert isinstance(result, float)
    assert 0.0 <= result <= 1.0


def test_sender_domain_normalizes_a_valid_address():
    assert sender_domain("offers@Deals.com") == "deals.com"


def test_first_link_returns_first_link_and_empty_when_missing():
    assert (
        first_link("See https://example.com/a then http://example.org")
        == "https://example.com/a"
    )
    assert first_link("No link here") == ""


def test_shout_ratio_handles_letters_and_no_letters():
    assert shout_ratio("FREE prize NOW") == 7 / 12
    assert shout_ratio("123 !?") == 0.0
