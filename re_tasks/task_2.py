import random
import re

from faker import Faker


def generate_data():
    fake = Faker()
    data_set = []

    for _ in range(50):
        fake_date = fake.date_of_birth()
        formatted_date = fake_date.strftime("%m/%d/%Y")
        data_set.append(str(random.choice([fake_date, formatted_date])))

    return data_set


def is_valid_date_format(date_string):
    date_pattern = re.compile(
        "(0?[1-9]|1[0-2])/(0?[1-9]|[1-2][0-9]|3[0-1])/([0-9]{4})$"
    )
    return bool(date_pattern.match(date_string))


if __name__ == "__main__":
    date_to_validate = generate_data()
    print(date_to_validate)

    split_data_set = date_to_validate
    counter = 0

    for i, date_str in enumerate(split_data_set):
        if is_valid_date_format(date_str):
            counter += 1
        else:
            print(f"Invalid data at index {i}: {date_str}")

    print(f"Number of correct dates: {counter}")
