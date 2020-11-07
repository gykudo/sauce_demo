from selenium.webdriver.common.by import By


class CheckoutCompleteLocator(object):
  COMPLETE_LABBEL = (By.XPATH, '//div[@class="checkout_complete_container"]/div[@class="complete-text"]')
  PONY_IMAGE = (By.XPATH, '//div[@class="checkout_complete_container"]/img[@class="pony-express"]')
