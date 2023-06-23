Feature: Accounts

    Scenario Outline: Account Currency Information
        When User clicks on button Select account
        When User selects the desired "<account>"
        Then Text "<Currency>" is displayed

        Examples:
            | account        | Currency |
            | EBQ11113487654 | EUR      |
            | EBQ11223487456 | EUR      |
            | EBQ11223387654 | EUR      |
            | EBQ38495629375 | USD      |
            | 511264340      | BTC      |









