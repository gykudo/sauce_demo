from selenium.webdriver.common.by import By


class LoginPageLocators(object):
  """A class for main page locators. All main page locators should come here"""
  INPUT_USERNAME = (By.ID, 'user-name')
  INPUT_PASSWORD = (By.ID, 'password')
  BUTTON_LOGIN = (By.ID, 'login-button')
  LABEL_MESSAGE = (By.XPATH, '//*[@id="login_button_container"]/div/form/h3')
