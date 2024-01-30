import pytest
from selene import browser


@pytest.fixture(scope="session")
def set_browser():
    browser.open('https://google.com')
    browser.config.window_width = 1920
    browser.config.window_height = 720
    yield
    browser.quit()


@pytest.fixture()
def clear_q():
    browser.element('[name="q"]').clear()
