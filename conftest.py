import pytest


@pytest.fixture(scope="session")
def browser():

    yield
