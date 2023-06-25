Feature: New Module

    @log_test
    Scenario: View News Details
        When User clicks on side menu "News"
        And User clicks on random news title
        Then Text "Back to List" is displayed