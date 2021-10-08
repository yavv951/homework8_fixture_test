import pytest


@pytest.fixture
def log(request, result):
    file_name = request.config.getoption("--logfile")
    with open(file_name, "a+") as f_obj:
        f_obj.write(f"test: {result}\n")
    yield
    f_obj.close()

def pytest_addoption(parser):
    parser.addoption(
        "--logfile",
        action="store",
        default="log.txt",
        help="File for recording test results",
    )


