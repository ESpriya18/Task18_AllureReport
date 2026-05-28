from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import allure

def before_scenario(context, scenario):

    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)



def after_scenario(context, scenario):

    if scenario.status == "failed" or scenario.status == "error":

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        screenshot_name = scenario.name.replace(" ", "_")

        screenshot_path = f"screenshots/{screenshot_name}.png"

        context.driver.save_screenshot(screenshot_path)

        allure.attach.file(
            screenshot_path,
            name=scenario.name,
            attachment_type=allure.attachment_type.PNG
        )

        print(f"Screenshot saved: {screenshot_path}")

    context.driver.quit()