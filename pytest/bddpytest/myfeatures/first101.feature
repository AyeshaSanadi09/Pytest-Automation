Feature : Bank Transactions
  Tests performing to banking transactions

  Scenario: Withdrawal of money
    Given the account balance is 100
    When the account holder withdraws 30
    Then the account balance should be 70

  Scenario: Removal of items from set
    Given a set of 3 fruits
    When we remove a fruit from the set
    Then the set will have 2 fruits