Feature: New Module

Scenario: View News Details
    When User clicks on side menu "News"
    And User clicks on random news title
    Then Text "Back to List" is displayed
