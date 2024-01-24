from re_tasks.task_5 import split_text_on_sentence


def test_split_text_on_sentence():
    text = "First sentence for test. And second sentence for test"
    empty = ""

    # Positive cases
    assert split_text_on_sentence(text) == [
        "First sentence for test.",
        "And second sentence for test",
    ]
    assert split_text_on_sentence("Only one sentence") == ["Only one sentence"]
    assert split_text_on_sentence("Text with punctuation marks!") == ["Text with punctuation marks!"]
    assert split_text_on_sentence("Text with punctuation marks?") == ["Text with punctuation marks?"]
    assert split_text_on_sentence("(@#$%^&*)! {<>}? [1,2,3,4,5,6,7,8,9,0].") == [
        "(@#$%^&*)!",
        "{<>}?",
        "[1,2,3,4,5,6,7,8,9,0].",
    ]

    # Negative case
    assert split_text_on_sentence(empty) == [""]
