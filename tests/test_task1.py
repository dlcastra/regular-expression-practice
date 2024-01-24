from re_tasks.task_1 import find_email_is_text


def test_find_email_is_text():
    correct_email = "Hello! My email is - stacey07@yahoo.com."
    email_without_name = "Hello! My email is - @yahoo.com."
    email_without_domain = "Hello! My email is - stacey07@."

    # Positive cases
    assert find_email_is_text(correct_email) == ["stacey07@yahoo.com"]
    assert find_email_is_text("Hello! I'm Stacey!07@yahoo.com hat's my e-mail address.") == ["07@yahoo.com"]
    assert find_email_is_text("Hello! I'm Stacey! My email is - stacey-07@yahoo.com.") == ["stacey-07@yahoo.com"]
    assert find_email_is_text("Hello! I'm Stacey! My email is - stacey-07@yahoo-privat.com.") == [
        "stacey-07@yahoo-privat.com"
    ]
    assert find_email_is_text("Hello! I'm Stacey! My email is - stacey_07@yahoo.com.") == ["stacey_07@yahoo.com"]
    assert find_email_is_text("Hello! I'm Stacey! My email is - stacey_07@yah_oo.com.") == ["stacey_07@yah_oo.com"]

    # Negative cases
    assert find_email_is_text(email_without_name) == []
    assert find_email_is_text(email_without_domain) == []
    assert find_email_is_text("Hello! Hello! I'm Stacey!") == []
    assert find_email_is_text("Hello! I'm Stacey!07@yahoo.com hat's my e-mail address.") != ["Stacey!07@yahoo.com"]

    assert find_email_is_text("Hello! My email is - stacey07@@yahoo.com.") == []
    assert find_email_is_text("Hello! My email is - stacey07@!yahoo.com.") == []
    assert find_email_is_text("Hello! My email is - stacey07@yah!oo.com.") == []
    assert find_email_is_text("Hello! My email is - stacey07@yah?oo.com.") == []
    assert find_email_is_text("Hello! My email is - stacey07@yah%oo.com.") == []
    assert find_email_is_text("Hello! My email is - stacey07@yah/oo.com.") == []
    assert find_email_is_text("Hello! My email is - stacey07@yah#oo.com.") == []
    assert find_email_is_text("Hello! My email is - stacey07@yah$oo.com.") == []
    assert find_email_is_text("Hello! My email is - stacey07@yah>oo.com.") == []
    assert find_email_is_text("Hello! My email is - stacey07@yah<oo.com.") == []
    assert find_email_is_text("Hello! My email is - stacey07@yah~oo.com.") == []

    assert find_email_is_text("Hello! My email is - sta(ce)y07@yah%oo.com.") == []
    assert find_email_is_text("Hello! My email is - sta[ce]y07@yah%oo.com.") == []
    assert find_email_is_text("Hello! My email is - sta{ce}y07@yah%oo.com.") == []
