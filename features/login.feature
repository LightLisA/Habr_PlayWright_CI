Feature: User login

  Scenario: Successful user login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should be logged in successfully
