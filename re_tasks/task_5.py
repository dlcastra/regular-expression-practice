import re

from faker import Faker


def generate_sentence():
    fake = Faker()
    sentences = ""
    sentences += " ".join([fake.sentence() for _ in range(10)])

    return sentences


def split_text_on_sentence(text):
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=[.?!])\s*", text)
    return sentences


if __name__ == "__main__":
    generated_sentence = generate_sentence()
    print(generated_sentence)
    print(split_text_on_sentence(generated_sentence))
