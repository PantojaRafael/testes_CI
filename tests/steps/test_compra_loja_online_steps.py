from pytest_bdd.parsers import parse

from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import Page

scenarios('../features/compra_loja_online.feature')

login = 'standard_user'
senha = 'secret_sauce'


@given("que esteja na página de login")
def user_is_on_login_page(browser: Page):
    browser.goto('https://www.saucedemo.com/')


@when(parse("preencho o campo com login e senha"), converters=dict(texto=str))
def preencher_campo_login_senha(browser: Page):
    browser.locator('[data-test="username"]').fill(login)
    browser.locator('[data-test="password"]').fill(senha)
    browser.locator('[data-test="login-button"]').click()


@when(parse("seleciono um produto e adiciono ao carrinho"), converters=dict(texto=str))
def seleciono_um_produto(browser: Page):
    browser.get_by_text('Sauce Labs Backpack').click()
    browser.get_by_text('Add to cart').click()


@when(parse("vejo o meu carrinho de compras"), converters=dict(texto=str))
def vejo_meu_carrinho_de_compras(browser: Page):
    browser.get_by_text('1').click()


@then(parse("a compra é realizada com sucesso"), converters=dict(texto=str))
def realizo_compra_com_sucesso(browser: Page):
    browser.get_by_text('CHECKOUT').click()

    # informacoes importantes de chekout

    browser.locator('[placeholder="First Name"]').fill('Rafael')
    browser.locator('[placeholder="Last Name"]').fill('Pantoja')
    browser.locator('[placeholder="Zip/Postal Code"]').fill('66073070')
    browser.get_by_text('CONTINUE').click()
