Feature: Cards Module

Scenario: View Cards
    When User clicks on side menu "Cards"
    Then Text "Card Number" is displayed
    Then Text "Card Holder" is displayed
    Then Text "Currency" is displayed