from selenium.webdriver.common.by import By


class LoginPageLocators(object):
  """A class for main page locators. All main page locators should come here"""
  INPUT_USERNAME = (By.ID, 'username')
  INPUT_PASSWORD = (By.ID, 'password')
  BUTTON_LOGIN = (By.ID, 'login-button')
  LABEL_MESSAGE = (By.ID, 'flash')
