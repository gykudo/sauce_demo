from Objects.product import Product
from Pages.base_page_object import BasePage
from Locators.product_detail_page_locator import ProductDetailPageLocator


class ProductsDetailsPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)

  def get_product_badge(self):
    total = 0
    try:
      total = self.get_text(ProductDetailPageLocator.SHOPPING_CART_LABEL)
    except Exception:
      pass
    return int(total)

  def get_product_info(self):
    name = self.get_text(ProductDetailPageLocator.PRODUCT_NAME_LABEL)
    desc = self.get_text(ProductDetailPageLocator.PRODUCT_DESC_LABEL)
    price = self.get_text(ProductDetailPageLocator.PRODUCT_PRICE_LABEL)
    return Product(name, desc, price)

  def add_product_to_cart(self):
    self.click(ProductDetailPageLocator.PRODUCT_ADD_BUTTON)

  def does_add_button_exist(self):
    return self.is_visible(ProductDetailPageLocator.PRODUCT_ADD_BUTTON)

  def remove_product_from_cart(self):
    self.click(ProductDetailPageLocator.PRODUCT_REMOVE_BUTTON)

  def does_remove_button_exist(self):
    return self.is_visible(ProductDetailPageLocator.PRODUCT_REMOVE_BUTTON)

  def is_product_badge_invisible(self):
    return self.is_invisible(ProductDetailPageLocator.SHOPPING_CART_LABEL)

  def back_to_product_page(self):
    self.click(ProductDetailPageLocator.BACK_BUTTON)

