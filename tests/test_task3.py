from re_tasks.task_3 import take_name_and_domain


def test_take_name_and_domain():
    correct_email = "I'm Stacey! My email is - stacey07@yahoo.com"
    incorrect_email = "I'm Stacey! My email is - stacey07@"

    # Positive cases
    assert take_name_and_domain(correct_email) == [("stacey07", "yahoo.com")]
    assert take_name_and_domain("stacey-07@yahoo.com") == [("stacey-07", "yahoo.com")]
    assert take_name_and_domain("stacey_07@yahoo.com") == [("stacey_07", "yahoo.com")]
    assert take_name_and_domain("stacey07@yah-oo.com") == [("stacey07", "yah-oo.com")]
    assert take_name_and_domain("stacey07@yah_oo.com") == [("stacey07", "yah_oo.com")]
    assert take_name_and_domain("stacey07@y.a.h.o.o.com") == [("stacey07", "y.a.h.o.o.com")]

    # Negative cases
    assert take_name_and_domain(incorrect_email) == []
    assert take_name_and_domain("") == []
    assert take_name_and_domain("I'm Stacey! I don't have e-mail") == []

    assert take_name_and_domain("Hello! My email is - stacey07@@yahoo.com.") == []
    assert take_name_and_domain("Hello! My email is - stacey07@!yahoo.com.") == []
    assert take_name_and_domain("Hello! My email is - stacey07@yah!oo.com.") == []
    assert take_name_and_domain("Hello! My email is - stacey07@yah?oo.com.") == []
    assert take_name_and_domain("Hello! My email is - stacey07@yah%oo.com.") == []
    assert take_name_and_domain("Hello! My email is - stacey07@yah/oo.com.") == []
    assert take_name_and_domain("Hello! My email is - stacey07@yah#oo.com.") == []
    assert take_name_and_domain("Hello! My email is - stacey07@yah$oo.com.") == []
    assert take_name_and_domain("Hello! My email is - stacey07@yah>oo.com.") == []
    assert take_name_and_domain("Hello! My email is - stacey07@yah<oo.com.") == []
    assert take_name_and_domain("Hello! My email is - stacey07@yah~oo.com.") == []
