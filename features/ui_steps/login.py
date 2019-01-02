from behave import *


@given("the admin has been created")
def step_admin_has_been_created(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("the admin browses to the login page")
def step_admin_browses_to_login_page(context):
    """
    :type context: behave.runner.Context
    """
    context.pages.get("login").open()


@step('the admin logs in with username "{username}" and email "{password}"')
def step_admin_logs_in(context, username, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
    context.pages.get("login").login(username, password)


@then("the user should be redirected to the Inbox Page")
def step_user_redirected_to_inbox_page(context):
    """
    :type context: behave.runner.Context
    """
    assert context.browser.title == "#Inbox - Zero"
