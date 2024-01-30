from pytest_bdd.parsers import parse

from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import Page

scenarios('../features/preencher_formulario.feature')


@given("que acesso o formulario")
def user_is_on_login_page(browser: Page):
    browser.goto('file:///C:/Users/rafael.pantoja/Desktop/formulario.html')


@given(parse("preencho os campos"), converters=dict(texto=str))
def preencho_os_campos(browser: Page):
    browser.locator('input[name="nome"]').fill('Rafael')
    browser.locator('input[name="email"]').fill('rafael.pantoja@fpf.br')
    browser.locator('input[name="senha"]').fill('123456')
    browser.get_by_text('Masculino').click()
    browser.locator('[id="mensagem"]').fill('Mensagem de teste')


@then(parse("clico em enviar"), converters=dict(texto=str))
def clico_em_enviar(browser: Page):
    browser.locator('[type="submit"]').click()



