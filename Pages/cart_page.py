from Locators.cart_page_locator import CartPageLocator
from Objects.product import Product
from Pages.base_page_object import BasePage
from Utils.utility import Utils


class CartPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)

  def get_product_info(self, index):
    name = self.get_text(CartPageLocator.PRODUCT_NAME_LABEL(index))
    desc = self.get_text(CartPageLocator.PRODUCT_DESC_LABEL(index))
    price = self.get_text(CartPageLocator.PRODUCT_PRICE_LABEL(index))
    qty = self.get_text(CartPageLocator.QTY_NUMBER_LABEL(index))
    return Product(name, desc, price, qty)

  def click_continue_shopping_button(self, index):
    self.click(CartPageLocator.CONTINUE_SHOPPINNG_BUTTON())

  def click_checkout_button(self):
    return self.click(CartPageLocator.CHECKOUT_BUTTON)

  def remove_product_from_cart(self, index):
    self.click(CartPageLocator.PRODUCT_REMOVE_BUTTON(index))

  def get_price(self, index):
    price_lbl = self.get_text(CartPageLocator.PRODUCT_PRICE_LABEL(index))
    price = Utils.convert_string_to_float(price_lbl)
    return float(price)


