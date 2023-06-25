Feature: My Profile

    @log_test
    Scenario: View Summary Section
        When User clicks on side menu "My Profile"
        Then Text "Summary" is displayed
