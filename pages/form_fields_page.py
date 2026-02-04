import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class FormFieldsPage:
    URL = "https://practice-automation.com/form-fields/"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # locators
    NAME = (By.ID, "name-input")
    PASSWORD = (By.XPATH, "//label[normalize-space()='Password']//input[@type='password']")
    DRINK_MILK = (By.CSS_SELECTOR, '[data-testid="drink2"]')
    DRINK_COFFEE = (By.CSS_SELECTOR, '[data-testid="drink3"]')
    COLOR_YELLOW = (By.CSS_SELECTOR, '[data-testid="color3"]')
    AUTOMATION_SELECT = (By.CSS_SELECTOR, '[data-testid="automation"]')
    EMAIL = (By.CSS_SELECTOR, '[data-testid="email"]')
    MESSAGE = (By.CSS_SELECTOR, '[data-testid="message"]')
    SUBMIT = (By.CSS_SELECTOR, '[data-testid="submit-btn"]')
    TOOLS_ITEMS = (By.XPATH, "//label[normalize-space()='Automation tools']/following-sibling::ul[1]/li")

    # helpers
    def _el(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _els(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    # actions with allure steps (Fluent)
    def open(self):
        with allure.step("Open form page"):
            self.driver.get(self.URL)
            self._el(self.NAME)
        return self

    def set_name(self, value: str):
        with allure.step(f"Set Name: {value}"):
            el = self._el(self.NAME)
            el.clear()
            el.send_keys(value)
        return self

    def set_password(self, value: str):
        with allure.step("Set Password"):
            el = self._el(self.PASSWORD)
            el.clear()
            el.send_keys(value)
        return self

    def choose_drinks(self):
        with allure.step("Choose drinks: Milk and Coffee"):
            self._el(self.DRINK_MILK).click()
            self._el(self.DRINK_COFFEE).click()
        return self

    def choose_color(self):
        with allure.step("Choose color: Yellow"):
            self._el(self.COLOR_YELLOW).click()
        return self

    def choose_like_automation(self, value: str = "yes"):
        with allure.step(f"Choose 'Do you like automation?': {value}"):
            select_el = self._el(self.AUTOMATION_SELECT)
            Select(select_el).select_by_value(value)
        return self

    def set_email(self, value: str):
        with allure.step(f"Set Email: {value}"):
            el = self._el(self.EMAIL)
            el.clear()
            el.send_keys(value)
        return self

    def build_message_from_tools(self) -> str:
        items = self._els(self.TOOLS_ITEMS)
        tools = [it.text.strip() for it in items if it.text and it.text.strip()]
        count = len(tools)
        longest = max(tools, key=len) if tools else ""
        return f"Automation tools count: {count}. Longest: {longest}"

    def set_message_auto(self):
        with allure.step("Set Message automatically from Automation tools list"):
            message = self.build_message_from_tools()
            el = self._el(self.MESSAGE)
            el.clear()
            el.send_keys(message)

            # прикрепим сам текст message (очень удобно в отчёте)
            allure.attach(message, name="generated_message", attachment_type=allure.attachment_type.TEXT)
        return self

    def attach_filled_form_screenshot(self, name: str = "filled_form_before_submit"):
        with allure.step("Attach filled form screenshot"):
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
        return self

    def submit(self):
        with allure.step("Submit form"):
            self._el(self.SUBMIT).click()
        return self

    def get_and_accept_alert_text(self) -> str:
        with allure.step("Read and accept alert"):
            alert = self.wait.until(EC.alert_is_present())
            text = alert.text
            alert.accept()
            allure.attach(text, name="alert_text", attachment_type=allure.attachment_type.TEXT)
            return text
