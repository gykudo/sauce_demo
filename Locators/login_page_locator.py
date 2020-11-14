from selenium.webdriver.common.by import By


class LoginPageLocators(object):
  """A class for main page locators. All main page locators should come here"""
  INPUT_USERNAME = (By.ID, 'user-name')
  INPUT_PASSWORD = (By.ID, 'password')
  BUTTON_LOGIN = (By.ID, 'login-button')
  ERR_MESS_LABEL = (By.XPATH, '//div[@id="login_button_container"]//h3[@class="err-button"]')
