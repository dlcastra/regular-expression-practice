from re_tasks.task_4 import is_valid_phone_number


def test_is_valid_phone_number():
    valid_phone_number = "+38 (066) 7209-7209"
    invalid_phone_number = "+38 (066) 7209-7209-7209"  # To many numbers

    # Positive cases
    assert is_valid_phone_number(valid_phone_number) is True
    assert is_valid_phone_number("+380667207209") is True
    assert is_valid_phone_number("+380 66 7209 909") is True
    assert is_valid_phone_number("+48 663 209 909") is True
    assert is_valid_phone_number("+38 (066) 7209 909") is True
    assert is_valid_phone_number("+380 (66) 7209 909") is True
    assert is_valid_phone_number("+380 (66) 7209-909") is True

    # Negative cases
    assert is_valid_phone_number(invalid_phone_number) is False
    assert is_valid_phone_number("") is False
    assert is_valid_phone_number("+380-(66)-7209-909") is False
    assert is_valid_phone_number("+380-66-7209-909") is False
    assert is_valid_phone_number("+380 66      7209 909") is False
    assert is_valid_phone_number("+ (66) 7209-909") is False
    assert is_valid_phone_number("380 66 7209 909") is False
    assert is_valid_phone_number("380 66") is False
    assert is_valid_phone_number("380 66 lalala") is False
