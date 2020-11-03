from selenium.webdriver.common.by import By


class CheckoutInforLocator(object):
  FIRSTNAME_TEXTBOX = (By.XPATH, '//div[@class="checkout_info_container"]//input[@id="first-name"]')
  LASTNAME_TEXTBOX = (By.XPATH, '//div[@class="checkout_info_container"]//input[@id="last-name"]')
  POSTALCODE_TEXTBOX = (By.XPATH, '//div[@class="checkout_info_container"]//input[@id="postal-code"]')
  CANCEL_BTN = (By.XPATH, '//div[@class="checkout_info_container"]//a[@class="cart_cancel_link btn_secondary"]')
  CONTINUE_BTN = (By.XPATH, '//div[@class="checkout_info_container"]//input[@value="CONTINUE"]')
