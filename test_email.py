import pytest
from func_verificate_email import valid_email


# Parametrize test for valid and unvalid email.
@pytest.mark.parametrize('email,result', [
    ('ttt@mail.ru', True),
    ('w@w.com', True),
    ('ggg@gmail.mmm', True)])
def test_valid_email(email, result, log):
    assert valid_email(email) == result, "Email is not valid"


@pytest.mark.parametrize('email,result', [
    ('test@test.', False),
    ('w@', False),
    ('@gmail.mmm', False)])
def test_unvalid_email(email, result, log):
    assert valid_email(email) == result, "Email is valid"
