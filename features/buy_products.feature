Feature: Buying a product

  Scenario: Successful buying products
    Given the user is logged in
    When the user adds a product to the cart
    And the user proceeds to checkout
    Then the product should be successfully purchased
