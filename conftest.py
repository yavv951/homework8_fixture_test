import pytest


@pytest.fixture
def log(result):
    """
    Write log to file
    :param result:
    """
    my_file = open("log.txt", "a+")
    my_file.write(f"valid test: {str(result)} \n")
    yield
    my_file.close()

@pytest.fixture
def log_un(result):
    """
    Write log to file
    :param result:
    """
    my_file = open("log.txt", "a+")
    my_file.write(f"unvalid test: {str(result)} \n")
    yield
    my_file.close()
