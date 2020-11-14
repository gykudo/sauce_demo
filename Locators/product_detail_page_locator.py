from selenium.webdriver.common.by import By


class ProductDetailPageLocator(object):
  PRODUCT_NAME_LABEL = (By.XPATH, '//div[@class="inventory_item_container"]//div[@class="inventory_details_name"]')
  PRODUCT_DESC_LABEL = (By.XPATH, '//div[@class="inventory_item_container"]//div[@class="inventory_details_desc"]')
  PRODUCT_PRICE_LABEL = (By.XPATH, '//div[@class="inventory_item_container"]//div[@class="inventory_details_price"]')
  PRODUCT_ADD_BUTTON = (By.XPATH, '//div[@class="inventory_item_container"]//button[text()="ADD TO CART"]')
  PRODUCT_REMOVE_BUTTON = (By.XPATH, '//div[@class="inventory_detail"]//button[text()="ADD TO CART"]')
  BACK_BUTTON = (By.XPATH, '//button[text()="<- Back"]')
  SHOPPING_CART_LABEL = (By.XPATH, '//div[@class="shopping_cart_container"]//span[@class="fa-layers-counter shopping_cart_badge"]')
