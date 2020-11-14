from selenium.webdriver.common.by import By


class CheckoutInforLocator(object):
  FIRSTNAME_TEXTBOX = (By.XPATH, '//div[@class="checkout_info_container"]//input[@id="first-name"]')
  LASTNAME_TEXTBOX = (By.XPATH, '//div[@class="checkout_info_container"]//input[@id="last-name"]')
  POSTALCODE_TEXTBOX = (By.XPATH, '//div[@class="checkout_info_container"]//input[@id="postal-code"]')
  CANCEL_BUTTON = (By.XPATH, '//div[@class="checkout_info_container"]//a[@class="cart_cancel_link BUTTON_secondary"]')
  CONTINUE_BUTTON = (By.XPATH, '//div[@class="checkout_info_container"]//input[@value="CONTINUE"]')
