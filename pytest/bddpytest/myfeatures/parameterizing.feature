@bddparam
Feature : Parameterizing tests in pytest BDD

  Scenario: check varities of fruits
    Given there are 3 varities of fruits
    When we add a same varity of fruit
    Then there is same count of varities
    But if we add a different varity of fruit
    Then the count of varities increases to 4

  @bddscenario
  Scenario: check varities of fruits
    Given Given there are 5 fruits
    When I eat 3 fruit
    And I eat 2 fruit
    Then I should have 0 fruits


