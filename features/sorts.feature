Feature: testing out some sorting algorithms

  Scenario: test bubble sort
    Given we run the app
    When we start the sort on an array of numbers [3, 23, 7, 1, 95, 58, 36]
    Then we will have 1 as first element