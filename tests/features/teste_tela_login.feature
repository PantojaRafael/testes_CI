# Created by rafael.pantoja at 30/01/2024
Feature: Acessar uma tela de login e validar o acesso

  Scenario: Acessar a tela de login
    Given que faco o acesso a tela de login
    When preencher o campo de usuário com "user"
    And preencher o campo de senha com "password" e clicar em "Entrar"
    Then devo ser redirecionado para a tela de home