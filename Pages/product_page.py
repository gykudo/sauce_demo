from Locators.product_page_locator import ProductPageLocator
from Pages.base_page_object import BasePage


class ProductPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)

  def check_product_existed(self):
    name_product = self.is_visible(ProductPageLocator.TEXT_PRODUCT_NAME)
    print(name_product)

