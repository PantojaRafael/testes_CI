from pytest_bdd.parsers import parse

from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import Page

scenarios('../features/captura_de_tela.feature')


@given("que estou na pagina do google")
def entro_page_google(browser: Page):
    browser.goto('https://www.google.com')


@then(parse("tiro uma foto e salvo"))
def faco_uma_captura(browser: Page):
    browser.screenshot(path='tests/screenshots/screenshot.png')