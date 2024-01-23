import re

from faker import Faker


def generate_text():
    fake = Faker()
    main_text = ""

    for i in range(30):
        sentence = fake.sentence()
        email = fake.ascii_email()
        words = sentence.split()
        main_text += (
            " ".join(
                [word if (i + 1) % 3 != 0 else email for i, word in enumerate(words)]
            )
            + " "
        )

    return main_text


def find_email_is_text(text):
    return re.findall(r"\S+@.\S+", text)


if __name__ == "__main__":
    generated_text = generate_text()
    emails = find_email_is_text(generated_text)
    print(f"Input text:\n{generated_text}\n\nAll emails in text:\n{emails}")
