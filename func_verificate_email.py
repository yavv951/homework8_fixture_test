import re


def valid_email(email):
    """
    Check is email correct
    :param email:
    :return: bool
    """
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))
