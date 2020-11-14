from Locators.products_page_locator import ProductsPageLocator
from Objects.product import Product
from Pages.base_page_object import BasePage


class ProductsPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    #products_page = ProductsPage(self.driver)

  def get_product_badge(self):
    total = 0
    try:
      total = self.get_text(ProductsPageLocator.SHOPPING_CART_LABEL)
    except Exception:
      pass
    return int(total)

  def get_product_info(self, index):
    name = self.get_text(ProductsPageLocator.PRODUCT_NAME_LABEL(index))
    desc = self.get_text(ProductsPageLocator.PRODUCT_DESC_LABEL(index))
    price = self.get_text(ProductsPageLocator.PRODUCT_PRICE_LABEL(index))
    return Product(name, desc, price)

  def get_broken_img(self):
    try:
      return self.get_elements_size(ProductsPageLocator.IMG_BROKEN)
    except Exception:
      return 0

  def add_product_to_cart(self, index):
    self.click(ProductsPageLocator.PRODUCT_ADD_BUTTON(index))

  def does_add_button_exist(self, index):
    return self.is_visible(ProductsPageLocator.PRODUCT_ADD_BUTTON(index))

  def remove_product_from_cart(self, index):
    self.click(ProductsPageLocator.PRODUCT_REMOVE_BUTTON(index))

  def does_remove_button_exist(self, index):
    return self.is_visible(ProductsPageLocator.PRODUCT_REMOVE_BUTTON(index))

  def is_product_badge_invisible(self):
    return self.is_invisible(ProductsPageLocator.SHOPPING_CART_LABEL)

  def click_product_cart(self):
    self.click(ProductsPageLocator.SHOPPING_CART_ITEM)

  def click_product_name(self, index):
    self.click(ProductsPageLocator.PRODUCT_NAME_LABEL(index))
