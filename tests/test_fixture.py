import pytest
from selene.support.shared import browser
from selene import command
from tests.data import open_site


@pytest.fixture(scope='function')
def browser_mobile():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 310
    browser.config._window_height = 516


@pytest.fixture(scope='function')
def browser_desktop():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1200
    browser.config._window_height = 800


def test_github_desktop(browser_desktop):
    open_site.element('.btn-mktg').click()


def test_github_mobile(browser_mobile):
    browser.open('https://github.com/')
    browser.element('.btn-mktg').click()
