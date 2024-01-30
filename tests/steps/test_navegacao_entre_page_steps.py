from pytest_bdd.parsers import parse

from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import Page

scenarios('../features/navegacao_entre_page.feature')


@given(parse("que vou entrando nas paginas uma por uma"), converters=dict(pulo=str))
def entro_na_page_google_e_bing(browser: Page):
    browser.goto('https://www.google.com.br/')
    browser.goto('https://www.bing.com/')
    browser.goto('https://www.apple.com/br/')
    browser.goto('https://br.yahoo.com/')


@then(parse("finalizo com a pagina do yahoo"), converters=dict(finalizo=str))
def entro_na_page_yahoo_e_faco_validacao(browser: Page):
    browser.goto('https://br.yahoo.com/')

