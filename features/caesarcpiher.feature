Feature: testing out caesar cipher

  Scenario: test caesar cipher #1
    Given we run the cipher
    When we start the cipher with offset of 8 on alphabet of abcdefghijklmnopqrstuvwxyz
    Then we will have ijklmnopqrstuvwxyzabcdefgh as result

  Scenario: test caesar cipher #2
    Given we run the cipher
    When we start the cipher with offset of -3 on alphabet of abcdefghijklmnopqrstuvwxyz
    Then we will have xyzabcdefghijklmnopqrstuvw as result

  Scenario: test caesar cipher #3
    Given we run the cipher
    When we start the cipher with offset of 8 on alphabet of qwertzuiopasdfghjklyxcvbnm
    Then we will have yemzbhcqwxialnoprstgfkdjvu as result

  Scenario: test caesar cipher #4
    Given we run the cipher
    When we start the cipher with offset of 5 on alphabet of asdasdasd
    Then we will have fxifxifxi as result

  Scenario: test caesar cipher #5
    Given we run the cipher
    When we start the cipher with offset of -3 on alphabet of qwertzuiopasdfghjklyxcvbnm
    Then we will have ntboqwrflmxpacdeghivuzsykj as result

  Scenario: test caesar cipher #6
    Given we run the cipher
    When we start the cipher with offset of 8 on alphabet of ""
    Then we will have "" as result

  Scenario: test caesar cipher #7
    Given we run the cipher
    When we start the cipher with offset of 0 on alphabet of abc
    Then we will have abc as result