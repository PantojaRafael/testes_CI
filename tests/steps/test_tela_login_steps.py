from pytest_bdd.parsers import parse

from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import Page

scenarios('../features/teste_tela_login.feature')

user = 'rafael.pantoja'
password = '@fpf2024'


@given("que faco o acesso a tela de login")
def user_is_on_login_page(browser: Page):
    browser.goto('https://bit.fpf.br/#/login')


@when(parse('preencher o campo de usuário com "user"'), converters=dict(texto=str))
def preencher_campo_usuario(browser: Page):
    browser.locator('[formcontrolname="username"]').fill(user)


@when(parse('preencher o campo de senha com "password" e clicar em "Entrar"'), converters=dict(texto=str))
def step_impl(browser: Page):
    browser.locator('[formcontrolname="password"]').fill(password)
    browser.locator('[type="submit"]').click()


@then("devo ser redirecionado para a tela de home")
def step_impl(browser: Page):
    expect(browser.get_by_text('PERFIL')).to_be_visible()

