Feature: testing out bubble sorting

  Scenario: test bubble sort #1
    Given we run the sort
    When we start the sort on an array of numbers [3, 23, 7, 1, 95, 58, 36]
    Then we will have 1 as first element

  Scenario: test bubble sort #2
    Given we run the sort
    When we start the sort on an array of numbers [-45, 56.7, 8532, -8542.53, 54523321]
    Then we will have -8542.53 as first element