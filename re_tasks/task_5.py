import re

from faker import Faker


def generate_sentence() -> str:
    """
    Generates 10 random sentences

    :return: str
        String with 10 randomly generated sentences.
    """
    fake = Faker()
    sentences = ""
    sentences += " ".join([fake.sentence() for _ in range(10)])

    return sentences


def split_text_on_sentence(text: str) -> list:
    """
    Split the input text into sentences.

    :param text: str
        The input text to be split into sentences.
    :return: List[str]
        A list of sentences extracted from the input text.
    """
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=[.?!])\s+", text)
    return sentences


if __name__ == "__main__":
    generated_sentence = generate_sentence()
    print(generated_sentence)
    print(split_text_on_sentence(generated_sentence))
