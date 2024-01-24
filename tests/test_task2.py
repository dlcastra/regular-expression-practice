from re_tasks.task_2 import is_valid_date_format


def test_is_valid_date_format():
    correct_date = "12/31/2024"
    incorrect_date = "31/12/2024"

    # Positive cases
    assert is_valid_date_format(correct_date) is True
    assert is_valid_date_format("01/01/2024") is True
    assert is_valid_date_format("10/10/2024") is True
    assert is_valid_date_format("10/10/0224") is True

    # Negative cases
    assert is_valid_date_format(incorrect_date) is False
    assert is_valid_date_format("") is False
    assert is_valid_date_format("10/10/1") is False
    assert is_valid_date_format("10/10/224") is False
    assert is_valid_date_format("00/00/0000") is False
    assert is_valid_date_format("00/10/2024") is False
    assert is_valid_date_format("10/00/2024") is False

    assert is_valid_date_format("month/10/2024") is False
    assert is_valid_date_format("10/day/2024") is False
    assert is_valid_date_format("10/10/year") is False

    assert is_valid_date_format("10 10 2024") is False
    assert is_valid_date_format("10-10-2024") is False
    assert is_valid_date_format("10:10:2024") is False
    assert is_valid_date_format("10\\10\\2024") is False

    assert is_valid_date_format("100/10/2024") is False
    assert is_valid_date_format("10/100/2024") is False
    assert is_valid_date_format("10/10/20244") is False

    assert is_valid_date_format("-1/10/20244") is False
    assert is_valid_date_format("10/-1/20244") is False
    assert is_valid_date_format("10/10/-2024") is False
