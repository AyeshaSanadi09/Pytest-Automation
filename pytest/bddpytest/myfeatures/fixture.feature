Feature : Fixtures and BDD background on python set datatype
  Background: Setting up data for test
    Given A datatpe set
    And the set is not empty

  Scenario: adding to a set
    Given a set of 3 elements
    When add 2 element to the set
    Then the set should have 5 elements