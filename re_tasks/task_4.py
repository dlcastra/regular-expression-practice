import re


def is_valid_phone_number(phone_number: str) -> bool:
    """
    Checks the validity of the entered phone number.

    :param phone_number: str
        Entered phone number for validity check.
    :return: bool
        True if the date format is valid, False otherwise.
    """
    pattern = re.compile(r"^\+(\d{1,3})\s?(\((\d{1,3})\)|(\d{1,3}))\s?(\d{3,4})\s?(\d{3,4}|-\d{3,4})$")

    match = pattern.match(phone_number)
    return bool(match and match.group(2))


if __name__ == "__main__":
    phone_numbers = [
        "+380667209909",
        "+380 66 7209 909",
        "+38 066 7209 909",
        "+38 (066) 7209 909",
        "+38 (066) 7209-909",
    ]
    for _phone_number in phone_numbers:
        if is_valid_phone_number(_phone_number):
            print(f"{_phone_number} - True")
        else:
            print(f"{_phone_number} - False")
