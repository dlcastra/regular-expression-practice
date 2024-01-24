import re

from faker import Faker


def generate_text() -> str:
    """
    Generates 30 random sentences in which every third word is an email address.

    :return: str
        String with fake text.
    """
    fake = Faker()
    main_text = ""

    for i in range(30):
        sentence = fake.sentence()
        email = fake.ascii_email()
        words = sentence.split()
        main_text += " ".join([word if (i + 1) % 3 != 0 else email for i, word in enumerate(words)]) + " "

    return main_text


def find_email_is_text(text: str) -> list:
    """
    Find valid email addresses in a sentence.

    :param text: str
        The input text containing email addresses.
    :return: List[str]
        A list of valid email addresses found in the text.
    """
    return re.findall(r"\b[A-z0-9._-]+@[A-z0-9.-]+\.[A-Z|a-z]{2,}\b(?!.*[!?#$%&*+=~<>])", text)


if __name__ == "__main__":
    generated_text = generate_text()
    emails = find_email_is_text(generated_text)
    print(f"Input text:\n{generated_text}\n\nAll emails in text:\n{emails}")
