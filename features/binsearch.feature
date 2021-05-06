Feature: testing out binary search

  Scenario: test binary search #1
    Given we run the search
    When we start the search for 8 on an array of numbers [3, 5, 8, 26, 58, 99]
    Then we will have 2 as result

  Scenario: test binary search #2
    Given we run the search
    When we start the search for 1 on an array of numbers [3, 5, 8, 26, 58, 99]
    Then we will have None as result

  Scenario: test binary search #3
    Given we run the search
    When we start the search for 58 on an array of numbers [3, 58, 5, 8, 26, 99]
    Then we will have None as result

  Scenario: test binary search #4
    Given we run the search
    When we start the search for -2.54 on an array of numbers [-95423814.4, -851, -52.4856324126, -2.54, 26, 99]
    Then we will have 3 as result

  Scenario: test binary search #5
    Given we run the search
    When we start the search for 1 on an array of numbers []
    Then we will have None as result
