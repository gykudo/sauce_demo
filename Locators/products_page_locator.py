from selenium.webdriver.common.by import By


class ProductsPageLocator(object):
  IMG_BROKEN = (By.XPATH, '//img[contains(@src, "jpgWithGarbageOnItToBreakTheUrl")]')
  SHOPPING_CART_LABEL = (By.XPATH, '//div[@id="shopping_cart_container"]//span[contains(@class,"shopping_cart_badge")]')
  SHOPPING_CART_ITEM = (By.XPATH, '//div[@id="shopping_cart_container"]')
  _PREFIX = '//div[@class="inventory_list"]/div[@class="inventory_item"]['

  def PRODUCT_NAME_LABEL(index):
    ITEM = ']//div[@class="inventory_item_name"]'
    return (By.XPATH, (ProductsPageLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_DESC_LABEL(index):
    ITEM = ']//div[@class="inventory_item_desc"]'
    return (By.XPATH, (ProductsPageLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_IMAGE(index):
    ITEM = ']//div[@class="inventory_item_img"]'
    return (By.XPATH, (ProductsPageLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_PRICE_LABEL(index):
    ITEM = ']//div[@class="inventory_item_price"]'
    return (By.XPATH, (ProductsPageLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_ADD_BUTTON(index):
    ITEM = ']//button[text()="ADD TO CART"]'
    return (By.XPATH, (ProductsPageLocator._PREFIX + str(index) + ITEM))

  def PRODUCT_REMOVE_BUTTON(index):
    ITEM = ']//button[text()="REMOVE"]'
    return (By.XPATH, (ProductsPageLocator._PREFIX + str(index) + ITEM))
