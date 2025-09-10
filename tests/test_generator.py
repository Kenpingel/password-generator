import string
import pytest

from passwords import generate_passwords


ALLOWED = set(string.ascii_letters + string.digits + string.punctuation)


def test_contains_lower_upper_digit_symbol():
    # Run multiple times to reduce flakiness
    for _ in range(10):
        p = generate_passwords()
        assert any(ch.islower() for ch in p)
        assert any(ch.isupper() for ch in p)
        assert any(ch.isdigit() for ch in p)
        assert any(ch in string.punctuation for ch in p)


def test_characters_come_from_allowed_pool():
    p = generate_passwords(32)
    assert all(ch in ALLOWED for ch in p)


def test_length_parameter_is_respected():
    for length in (4, 8, 12, 24, 40):
        p = generate_passwords(length=length)
        assert len(p) == length
        

@pytest.mark.xfail(reason="Length validation not implemented yet")
@pytest.mark.parametrize("invalid_length", [0, 1, 2, 3, -5])
def test_length_less_than_4_raises(invalid_length):
    with pytest.raises(ValueError, match="length must be at least 4"):
            generate_passwords(length=invalid_length)


@pytest.mark.xfail(reason="Exclude digits option not implemented yet")
def test_excluding_digits_produces_no_digits():
    # Future API idea: passwords(length=16, include_digits=False)
    p = generate_passwords(length=16, include_digits=False)  # type: ignore[call-arg]
    assert not any(ch.isdigit() for ch in p)


@pytest.mark.xfail(reason="Exclude symbols option not implemented yet")
def test_excluding_symbols_produces_no_symbols():
    # Future API idea: passwords(length=16, include_symbols=False)
    p = generate_passwords(length=16, include_symbols=False)  # type: ignore[call-arg]
    assert not any(ch in string.punctuation for ch in p)
