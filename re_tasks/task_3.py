import re

from task_1 import generate_text, find_email_is_text


def take_name_and_domain(text):
    pattern = re.compile(r"([A-z0-9._%+-]+)@([A-z0-9.-]+)")
    find_data = pattern.findall(text)

    return find_data


if __name__ == "__main__":
    generated_text = generate_text()
    emails = find_email_is_text(generated_text)
    result = take_name_and_domain(generated_text)
    print(f"Full text:\n{generated_text}\n\nList of emails:\n{emails}\n\nResult:\n{result}")
