from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class DashboardPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)



    profile_icon = (
        By.XPATH,
        "//div[contains(@class,'profile-click-icon-div')]"
    )



    logout_button = (
        By.XPATH,
        "//li[contains(text(),'Log out')]"
    )



    close_popup_button = (
        By.XPATH,
        "//button//*[name()='svg']"
    )

    @allure.step("Logout from portal")
    def logout(self):

        wait = WebDriverWait(self.driver, 20)


        try:
            close_popup = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(@class,'MuiIconButton-root')]")
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                close_popup
            )

            wait.until(
                EC.invisibility_of_element_located(
                    (By.CLASS_NAME, "MuiBackdrop-root")
                )
            )

        except TimeoutException:
            print("Popup not displayed")


        profile = wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "profile-click-icon-div")
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            profile
        )


        logout_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[normalize-space()='Log out']")
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            logout_btn
        )
