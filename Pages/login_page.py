from Locators.login_page_locator import LoginPageLocators
from Pages.base_page_object import BasePage
from TestData.TestData import TestData


class LoginPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.navigate_to(TestData.BASEURL)

  def login(self, username, password):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, username)
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, password)
    self.click(LoginPageLocators.BUTTON_LOGIN)

  def get_err_message(self):
    return self.get_text(LoginPageLocators.ERR_MESS_LBL)
