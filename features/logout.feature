Feature: Logout Functionality

  Scenario: Validate logout functionality
    Given user logged into the portal
    When user clicks logout button
    Then user should logout successfully