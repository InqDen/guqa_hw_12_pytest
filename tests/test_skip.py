import pytest
from selene.support.shared import browser
from data import open_site


@pytest.fixture(params=[(1280, 1024), (1024, 768), (420, 768), (320, 768)])
def browser_size(request):
    return request


@pytest.fixture(scope='function', autouse=True)
def browser_config(browser_size):
    browser.open('https://github.com/')
    width = browser_size.param[0]
    height = browser_size.param[1]
    browser.driver.set_window_size(width=width, height=height)


def test_github_desktop(browser_size):
    if browser.driver.get_window_size()["width"] < 1010:
        pytest.skip('Size for mobile version')
    browser.element('.btn-mktg').click()


def test_github_mobile():
    if browser.driver.get_window_size()["width"] > 1011:
        pytest.skip('Size for desktop version')
    browser.element('.btn-mktg').click()