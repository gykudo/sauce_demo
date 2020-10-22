from selenium.webdriver.common.by import By


class ProductPageLocator(object):
  ICONN_MENU = (By.XPATH, '//*[@id="menu_button_container"]/div/div[2]')
  LINK_ALL_ITEM = (By.ID, 'inventory_sidebar_link')
  LINK_ABOUT = (By.ID, 'about_sidebar_link')
  LINK_LOGOUT = (By.ID, 'logout_sidebar_link')
  TEXT_PRODUCT_NAME = (By.XPATH, "//div[@class='inventory_list']/div[@class='inventory_item'][1]//div["
                                 "@class='inventory_item_name']")
  BTN_ADD = (By.XPATH, "")