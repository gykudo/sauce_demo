from Locators.product_page_locator import ProductPageLocator
from Objects.product import Product
from Pages.base_page_object import BasePage


class ProductPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)

  def get_product_info(self, index):
    name = self.get_text(ProductPageLocator.PRODUCT_NAME_LABEL(index))
    desc = self.get_text(ProductPageLocator.PRODUCT_DESC(index))
    price = self.get_text(ProductPageLocator.PRODUCT_PRICE_LABEL(index))
    return Product(name, desc, price)

  def get_broken_img(self):
    try:
      return self.get_elements_size(ProductPageLocator.IMG_BROKEN)
    except Exception:
      return 0

  def add_product_to_cart(self, index):
    self.click(ProductPageLocator.PRODUCT_ADD_BUTTON(index))

  def remove_product_from_cart(self, index):
    self.click(ProductPageLocator.PRODUCT_REMOVE_BUTTON(index))
