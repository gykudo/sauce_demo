from selenium.webdriver.common.by import By


class CheckoutOverviewLocator(object):

  SUMMARY_TEXT = (By.XPATH, '//div[@class="summary_info"]//div[@class="summary_value_label"]')

  _PREFIX = '//div[@class="cart_list"]/div[@class="cart_item"]['


  def QTY_NUMBER_LABEL(index):
    ITEM = ']/div[@class="summary_quantity"]'
    return (By.XPATH, (CheckoutOverviewLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_NAME_LABEL(index):
    ITEM = "]//div[@class='inventory_item_name']"
    return (By.XPATH, (CheckoutOverviewLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_DESC_LABEL(index):
    ITEM = "]//div[@class='inventory_item_desc']"
    return (By.XPATH, (CheckoutOverviewLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_PRICE_LABEL(index):
    ITEM = "]//div[@class='inventory_item_price']"
    return (By.XPATH, (CheckoutOverviewLocator._PREFIX + str(index) + ITEM))