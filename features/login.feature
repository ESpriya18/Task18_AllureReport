Feature: Zen Portal Login Functionality

  Scenario: Successful Login
    Given user launches the browser
    When user opens the zen portal
    And user enters valid username and password
    And user clicks login button
    Then user should login successfully

  Scenario: Unsuccessful Login
    Given user launches the browser
    When user opens the zen portal
    And user enters invalid username and password
    And user clicks login button
    Then login should fail

  Scenario: Validate username and password fields
    Given user launches the browser
    When user opens the zen portal
    Then username and password fields should be visible

  Scenario: Validate submit button
    Given user launches the browser
    When user opens the zen portal
    Then login button should be enabled