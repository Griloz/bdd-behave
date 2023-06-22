# similar to Epic name
Feature: Login

# similar to user stories, test cases
@smoke
Scenario: Login with valid username and valid password
    When User enters valid username
    And User enters valid password
    And User clicks on login button
    Then Home page displays

@smoke
Scenario: Logout from the app
    When User clicks on logout button
    Then Login page displays


Scenario Outline: Login with invalid username and password combination
    When User enters username "<username>"
    And User enters password "<password>"
    And User clicks on login button
    Then Text "<text>" is displayed

    Examples:
        | username  | password  | text                          |
        | test      | test      | Wrong username or password    |
        | ^&^%      | *&^@      | Wrong username or password    |
        | aa        | test      | Should be minimum 4 chars     |
        | blank     | test      | Field is required             |
        | test      | blank     | Field is required             |