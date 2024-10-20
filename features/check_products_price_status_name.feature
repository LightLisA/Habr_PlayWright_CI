Feature: Product verification

  Scenario Outline: Verify product details
    Given the user is logged in
    When the user navigates to the product page of "<product_name>"
    Then the product name should be "<expected_product_name>"
    And the product description should be "<expected_description>"
    And the product price should be "<expected_price>"

  Examples:
    | product_name             | expected_product_name    | expected_description                                                                                                                                                   | expected_price |
    | Sauce Labs Backpack      | Sauce Labs Backpack      | with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.                                                      | $29.99         |
    | Sauce Labs Bike Light    | Sauce Labs Bike Light    | A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.        | $9.99          |
    | Sauce Labs Bolt T-Shirt  | Sauce Labs Bolt T-Shirt  | Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.                        | $15.99         |
    | Sauce Labs Fleece Jacket | Sauce Labs Fleece Jacket | It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office. | $49.99         |
    | Sauce Labs Onesie        | Sauce Labs Onesie        | Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.        | $7.99          |
    | T-Shirt (Red)            | T-Shirt (Red)            | This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.              | $15.99         |



