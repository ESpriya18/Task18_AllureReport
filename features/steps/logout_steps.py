from behave import *
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time

VALID_USER = "aespriya@gmail.com"
VALID_PASS = "Guvi*hcl@1610"

@given("user logged into the portal")
def step_impl(context):

    login = LoginPage(context.driver)

    login.open_url()

    login.enter_username(VALID_USER)
    login.enter_password(VALID_PASS)
    login.click_login()

    time.sleep(5)

@when("user clicks logout button")
def step_impl(context):

    dashboard = DashboardPage(context.driver)

    dashboard.logout()

@then("user should logout successfully")
def step_impl(context):

    time.sleep(3)

    assert "login" in context.driver.current_url.lower()