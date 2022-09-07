from selene import browser, have


def test_open_and_search():
    browser.open('https://github.com')
    browser.element('.btn-mktg').click()
    #browser.element('.sr-only').should(have.exact_text('Welcome to GitHub!'))
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))