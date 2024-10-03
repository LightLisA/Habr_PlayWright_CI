Feature: User login

  Scenario Outline: Successful user login
    Given the user is on the login page
    When the user enters valid credentials <login> and <password>
    Then the user should be logged in <successfully>

    Examples:
      | login           | password      | successfully  |
      | locked_out_user | secret_sauce  | NO            |
      | error_user      | secret_sauce  | YES           |
      | AUTH_LOGIN      | AUTH_PASSWORD | YES           |