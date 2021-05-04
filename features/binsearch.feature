Feature: testing out binary search

  Scenario: test binary search #1
    Given we run the search
    When we start the search for 8 on an array of numbers [3, 5, 8, 26, 58, 99]
    Then we will have 2 as result

  Scenario: test binary search #2
    Given we run the search
    When we start the search for 1 on an array of numbers [3, 5, 8, 26, 58, 99]
    Then we will have None as result