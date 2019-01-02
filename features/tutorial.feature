Feature: Login
  As a user
  I should be able to login

  @wip
  @fixture.browser
  Scenario: User logs in with correct password
    Given the admin has been created
    When the admin browses to the login page
    And the admin logs in with username "jpt@jpt.co" and email "admin"
    Then the user should be redirected to the Inbox Page
