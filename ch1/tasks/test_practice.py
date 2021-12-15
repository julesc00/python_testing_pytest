
def test_num_in_lst():
    """Assert value in list."""
    lst = ["hello", "nice", True]

    assert "hello" in lst


def test_qty():
    """Assert qty is equal to."""
    qty = 90

    assert qty >= 90


def test_txt_in_msg():
    """Assert if text is in message."""
    txt = "fizz"
    txt2 = "fizzbuzz"
    assert txt in txt2
