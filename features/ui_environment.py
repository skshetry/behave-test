import os

from behave import fixture, use_fixture
from splinter.browser import Browser

from pages.search_page import SearchPage

@fixture
def browser(context):
    user_data = context.config.userdata
    driver = user_data.get("driver", "chrome")
    kwargs = {
        "driver_name": driver
    }
    if driver == "remote":
        selenium_url = os.environ.get("SELENIUM_URL") or user_data.get("selenium_url", "http://localhost:4444/wd/hub")
        kwargs.update({"url": selenium_url, "driver_name": "remote", "browser": "chrome"})

    print(kwargs)
    context.browser = Browser(**kwargs)
    if os.environ.get("CI"):
        print("View SauceLabs jobs at: https://saucelabs.com/jobs/{}".format(context.browser.driver.session_id))
    yield context.browser

    # CLEANUP
    context.browser.quit()


@fixture
def get_pages(context):
    print(context.config.userdata)
    base_url = context.config.userdata.get("base_url", "http://localhost:8069")
    context.pages = {
        "search": SearchPage(context.browser, base_url=base_url)
    }
    return context.pages


def before_all(context):
    use_fixture(browser, context)


def before_tag(context, tag):
    if "fixture.browser" in tag:
        use_fixture(get_pages, context)
