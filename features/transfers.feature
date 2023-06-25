Feature: Transfers section

    User should be able to pass to Transfers section page and click any transfer option.

    Background: Go to Transfer sections
        When User clicks on side menu "Transfers"

    @transfers_options @regression
    Scenario: View Transfers section
        # When User clicks on side menu "Transfers"
        Then Text "Transfer Between Accounts" is displayed
        Then Text "Transfer Between Users" is displayed
        Then Text "Outgoing Wire Transfer" is displayed
        Then Text "SEPA Transfer" is displayed
        Then Text "Card Funding Transfer" is displayed
        Then Text "Incoming Wire Transfer" is displayed

    @transfers_options @regression
    Scenario: View Transfer Between Accounts option
        # When User clicks on side menu "Transfers"
        When User clicks "Transfer Between Accounts" option
        Then Text "Transfer Between Accounts" is displayed
        Then Text "Select account" is displayed
        Then Text "Amount to transfer" is displayed
        Then Text "Description" is displayed
        Then Text "Cancel" is displayed
        Then Text "Continue" is displayed


    @transfers_options
    Scenario: View Transfer Between Users option
        # When User clicks on side menu "Transfers"
        When User clicks "Transfer Between Users" option
        Then Text "Transfer Between Users" is displayed
        Then Text "Select account" is displayed
        Then Text "Credit to" is displayed
        Then Text "Username" is displayed
        Then Text "Account" is displayed
        Then Text "Amount to transfer" is displayed
        Then Text "Description" is displayed
        Then Text "Upload Supporting Documentation" is displayed
        Then Text "Cancel" is displayed
        Then Text "Continue" is displayed


    @transfers_options
    Scenario: View Outgoing Wire Transfer option
        # When User clicks on side menu "Transfers"
        When User clicks "Outgoing Wire Transfer" option
        Then Text "Outgoing Wire Transfer" is displayed
        Then Text "Select account" is displayed
        Then Text "Beneficiary Bank" is displayed
        Then Text "Beneficiary Customer" is displayed
        Then Text "Additional Information" is displayed
        Then Text "Transfer Details" is displayed
        Then Text "Description" is displayed
        Then Text "Cancel" is displayed
        Then Text "Continue" is displayed


    @transfers_options
    Scenario: View Card Funding Transfer option
        # When User clicks on side menu "Transfers"
        When User clicks "Card Funding Transfer" option
        Then Text "Card Funding Transfer" is displayed
        Then Text "Select account" is displayed
        Then Text "Description" is displayed
        Then Text "Cancel" is displayed
        Then Text "Continue" is displayed


    @transfers_options
    Scenario: View Incoming Wire Transfer option
        # When User clicks on side menu "Transfers"
        When User clicks "Incoming Wire Transfer" option
        Then Text "Incoming Wire Transfer" is displayed
        Then Text "Select account" is displayed
        Then Text "Cancel" is displayed
        Then Text "Continue" is displayed