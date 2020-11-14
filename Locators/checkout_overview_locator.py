from selenium.webdriver.common.by import By


class CheckoutOverviewLocator(object):
  SUMMARY_LABEL = (By.XPATH, '//div[@class="summary_info"]//div[@class="summary_value_label"]')
  TOTAL_ITEM_PRICE_LABEL = (By.XPATH, '//div[@class="summary_info"]/div[@class="summary_subtotal_label"]')
  TAX_LABEL = (By.XPATH, '//div[@class="summary_info"]/div[@class="summary_tax_label"]')
  TOTAL_PRICE_LABEL = (By.XPATH, '//div[@class="summary_info"]/div[@class="summary_total_label"]')
  FINISH_BUTTON = (By.XPATH, '//div[@class="summary_info"]//a[text()="FINISH"]')
  _PREFIX = '//div[@class="cart_list"]/div[@class="cart_item"]['

  def PRODUCT_QTY_LABEL(index):
    ITEM = ']/div[@class="summary_quantity"]'
    return (By.XPATH, (CheckoutOverviewLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_NAME_LABEL(index):
    ITEM = ']//div[@class="inventory_item_name"]'
    return (By.XPATH, (CheckoutOverviewLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_DESC_LABEL(index):
    ITEM = ']//div[@class="inventory_item_desc"]'
    return (By.XPATH, (CheckoutOverviewLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_PRICE_LABEL(index):
    ITEM = ']//div[@class="inventory_item_price"]'
    return (By.XPATH, (CheckoutOverviewLocator._PREFIX + str(index) + ITEM))
