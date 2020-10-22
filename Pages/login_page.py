from Locators.login_page_locator import LoginPageLocators
from Pages.base_page_object import BasePage
from TestData.TestData import TestData


class LoginPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.navigate_to(TestData.BASEURL)

  def login(self, account):
    self.enter_username(account.username)
    self.enter_password(account.password)
    self.click_login_button()

  def enter_username(self, username):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, username)

  def enter_password(self, password):
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, password)

  def click_login_button(self):
    self.click(LoginPageLocators.BUTTON_LOGIN)

  def get_message(self):
    return self.get_text(LoginPageLocators.LABEL_MESSAGE)
