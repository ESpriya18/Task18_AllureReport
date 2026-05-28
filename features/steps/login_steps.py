from behave import *
from pages.login_page import LoginPage
import allure
import time

VALID_USER = "aespriya@gmail.com"
VALID_PASS = "Guvi*hcl@1610"


@given("user launches the browser")
def step_impl(context):
    pass

@when("user opens the zen portal")
def step_impl(context):
    context.login = LoginPage(context.driver)
    context.login.open_url()

@when("user enters valid username and password")
def step_impl(context):
    context.login.enter_username(VALID_USER)
    context.login.enter_password(VALID_PASS)

@when("user enters invalid username and password")
def step_impl(context):
    context.login.enter_username("wrong@gmail.com")
    context.login.enter_password("wrong123")

@when("user clicks login button")
def step_impl(context):
    context.login.click_login()
    time.sleep(5)

@then("user should login successfully")
def step_impl(context):
    assert "dashboard" in context.driver.current_url.lower()

@then("login should fail")
def step_impl(context):
    assert "login" in context.driver.current_url.lower()

@then("username and password fields should be visible")
def step_impl(context):
    assert context.login.validate_input_fields()

@then("login button should be enabled")
def step_impl(context):
    assert context.login.validate_login_button()