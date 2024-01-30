from selene import browser, be, have, by


def test_selene_can_be_found(set_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()

    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_selene_no_results(set_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()