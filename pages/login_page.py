from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    username_textbox = (
        By.XPATH,
        "//input[@placeholder='Enter your mail']"
    )

    password_textbox = (
        By.XPATH,
        "//input[@type='password']"
    )

    login_button = (
        By.XPATH,
        "//button[@type='submit']"
    )

    @allure.step("Open Zen Portal")
    def open_url(self):
        self.driver.get("https://v2.zenclass.in")

        self.driver.maximize_window()

        self.wait.until(
            lambda driver: driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    @allure.step("Enter Username")
    def enter_username(self, username):
        username_element = self.wait.until(
            EC.presence_of_element_located(
                self.username_textbox
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            username_element
        )

        self.wait.until(
            EC.visibility_of(username_element)
        )

        username_element.clear()

        username_element.send_keys(username)

    @allure.step("Enter Password")
    def enter_password(self, password):
        password_element = self.wait.until(
            EC.presence_of_element_located(
                self.password_textbox
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            password_element
        )

        self.wait.until(
            EC.visibility_of(password_element)
        )

        password_element.clear()

        password_element.send_keys(password)

    @allure.step("Click Login Button")
    def click_login(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.login_button
            )
        ).click()

    def validate_input_fields(self):

        username = self.wait.until(
            EC.visibility_of_element_located(
                self.username_textbox
            )
        )

        password = self.wait.until(
            EC.visibility_of_element_located(
                self.password_textbox
            )
        )

        return (
            username.is_displayed()
            and
            password.is_displayed()
        )

    def validate_login_button(self):

        login_btn = self.wait.until(
            EC.visibility_of_element_located(
                self.login_button
            )
        )

        return login_btn.is_enabled()