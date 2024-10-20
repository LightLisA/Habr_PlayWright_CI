Feature: User login

  Scenario Outline: Successful user login
    Given the user is on the login page
    When the user enters valid credentials <login> and <password>
    Then the user should be logged in successfully

    Examples: Work users
      | login      | password      |
      | error_user | secret_sauce  |
      | AUTH_LOGIN | AUTH_PASSWORD |


  Scenario: Unsuccessful user login
    Given the user is on the login page
    When the user enters valid credentials locked_out_user and secret_sauce
    Then the user should be logged in with warning
