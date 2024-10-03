Feature: Buying a product

  Scenario Outline: Successful buying products
    Given the user is logged in
    When the user adds a product to the cart
    And the user proceeds to checkout with "<first_name>" and "<last_name>" and "<zip>"
    Then the product should be successfully purchased

  Examples:
    | first_name | last_name | zip    |
    | Oleksa     | Gudko     | 123456 |
