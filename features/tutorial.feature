Feature: Login
  As a user
  I should be able to login

  @wip
  @fixture.browser
  Scenario: User searches cats
    When the admin browses to the search page
    And the user searches for "cats"
    Then the user should be redirected to homepage
