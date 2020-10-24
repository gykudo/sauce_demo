from selenium.webdriver.common.by import By


class ProductPageLocator(object):
  ICONN_MENU = (By.XPATH, '//*[@id="menu_button_container"]/div/div[2]')
  LINK_ALL_ITEM = (By.ID, 'inventory_sidebar_link')
  LINK_ABOUT = (By.ID, 'about_sidebar_link')
  LINK_LOGOUT = (By.ID, 'logout_sidebar_link')
  PREFIX = "//div[@class='inventory_list']/div[@class='inventory_item']["
  IMG_BROKEN = (By.XPATH, '//img[contains(@src, "jpgWithGarbageOnItToBreakTheUrl")]')

  def PRODUCT_NAME_LABEL(index):
    ITEM = "]//div[@class='inventory_item_name']"
    return (By.XPATH, (ProductPageLocator.PREFIX + str(index) + ITEM))

  def PRODUCT_ADD_BUTTON(index):
    ITEM = "]//button[text()='ADD TO CART']"
    return (By.XPATH, (ProductPageLocator.PREFIX + str(index) + ITEM))

  def PRODUCT_PRICE_LABEL(index):
    ITEM = "]//div[@class='inventory_item_price']"
    return (By.XPATH, (ProductPageLocator.PREFIX + str(index) + ITEM))

  def PRODUCT_IMAGE(index):
    ITEM = "]//div[@class='inventory_item_img']"
    return (By.XPATH, (ProductPageLocator.PREFIX + str(index) + ITEM))

  def PRODUCT_REMOVE_BUTTON(index):
    ITEM = "]//button[text()='REMOVE']"
    return (By.XPATH, (ProductPageLocator.PREFIX + str(index) + ITEM))

  def PRODUCT_DESC(index):
    ITEM = "]//div[@class='inventory_item_desc']"
    return (By.XPATH, (ProductPageLocator.PREFIX + str(index) + ITEM))
