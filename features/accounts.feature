Feature: Accounts

    Scenario Outline: Account Currency Information
        When User clicks on button Select account
        When User selects the desired "<account>"
        Then Text "<Account number matches>" is displayed
        Then Text "<Currency>" is displayed
        Then Text "<Account type>" is displayed
        Then Text "<Status>" is displayed

        Examples:
            | account        | Account number matches | Currency | Account type | Status |
            | EBQ11113487654 | EBQ11113487654         | EUR      | Checking     | Active |
            | EBQ11223487456 | EBQ11223487456         | EUR      | Savings      | Active |
            | EBQ11223387654 | EBQ11223387654         | EUR      | Savings      | Active |
            | EBQ38495629375 | EBQ38495629375         | USD      | Checking     | Active |
            | 511264340      | 511264340              | BTC      | BTC Wallet   | Active |