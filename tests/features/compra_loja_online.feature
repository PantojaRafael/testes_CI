# Created by rafael.pantoja at 30/01/2024
Feature: Fazer login em um siste e realizar uma compra

  Scenario: fazer login em um site e realizar uma compra
    Given que esteja na página de login
    When preencho o campo com login e senha
    When seleciono um produto e adiciono ao carrinho
    When vejo o meu carrinho de compras
    Then a compra é realizada com sucesso
