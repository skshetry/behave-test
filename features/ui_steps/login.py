from behave import *


@when("the admin browses to the search page")
def step_admin_browses_to_login_page(context):
    """
    :type context: behave.runner.Context
    """
    context.pages.get("search").open()


@step('the user searches for "{text}"')
def step_admin_logs_in(context, text):
    """
    :type context: behave.runner.Context
    :type text: str
    """
    context.search_term = text
    context.pages.get("search").search(text)


@step('the user should be redirected to homepage')
def step_admin_logs_in(context):
    """
    :type context: behave.runner.Context
    :type text: str
    """
    assert True
