from behave import fixture, use_fixture
from splinter.browser import Browser

from pages.login_page import LoginPage


@fixture
def browser_chrome(context):
    # -- SETUP-FIXTURE PART:
    context.browser = Browser("chrome")
    print("jejeje")
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


@fixture
def get_pages(context):
    context.pages = {"login": LoginPage(context.browser)}
    print(context.pages)
    return context.pages


def before_feature(context, feature):
    use_fixture(browser_chrome, context)
    use_fixture(get_pages, context)
