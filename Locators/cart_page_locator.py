from selenium.webdriver.common.by import By


class CartPageLocator(object):
  CARTITEM = (By.XPATH, '//*[@id="shopping_cart_container"]/a/svg')
  _PREFIX = '//div[@class="cart_list"]/div[@class="cart_item"]['
  CONTINUE_SHOPPINNG_BUTTON = (By.XPATH, '//a[text()="CONTINUE SHOPPING"]')
  CHECKOUT_BUTTON = (By.XPATH, '//a[text()="CHECKOUT"]')

  def QTY_NUMBER_LABEL(index):
    ITEM = ']/div[@class="cart_quantity"]'
    return (By.XPATH, (CartPageLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_NAME_LABEL(index):
    ITEM = "]//div[@class='inventory_item_name']"
    return (By.XPATH, (CartPageLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_DESC_LABEL(index):
    ITEM = "]//div[@class='inventory_item_desc']"
    return (By.XPATH, (CartPageLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_PRICE_LABEL(index):
    ITEM = "]//div[@class='inventory_item_price']"
    return (By.XPATH, (CartPageLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_REMOVE_BUTTON(index):
    ITEM = "]//button[text()='REMOVE']"
    return (By.XPATH, (CartPageLocator._PREFIX + str(index) + ITEM))


