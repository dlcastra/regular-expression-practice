import re

from re_tasks.task_1 import generate_text, find_email_is_text


def take_name_and_domain(text: str) -> list:
    """
    Extract username and domain from email addresses in the given text.

    :param text: str
        The input text containing email addresses.
    :return: List[Tuple[str, str]]
        A list of tuples, each containing the username and domain parts of an email address.
    """
    pattern = re.compile(r"\b([A-z0-9.-]+)@([A-z0-9.-]+)\b(?!.*[!?#$%&*+=~<>\\/])")
    find_data = pattern.findall(text)

    return find_data


if __name__ == "__main__":
    generated_text = generate_text()
    emails = find_email_is_text(generated_text)
    result = take_name_and_domain(generated_text)
    print(f"Full text:\n{generated_text}\n\nList of emails:\n{emails}\n\nResult:\n{result}")
