from Locators.checkout_overview_locator import CheckoutOverviewLocator
from Objects.product import Product
from Pages.base_page_object import BasePage
from Utils.utility import Utils


class CheckoutOverViewPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)

  def get_product_overview_info(self, index):
    name = self.get_text(CheckoutOverviewLocator.PRODUCT_NAME_LABEL(index))
    desc = self.get_text(CheckoutOverviewLocator.PRODUCT_DESC_LABEL(index))
    price = self.get_text(CheckoutOverviewLocator.PRODUCT_PRICE_LABEL(index))
    qty = self.get_text(CheckoutOverviewLocator.PRODUCT_QTY_LABEL(index))
    return Product(name, desc, price, qty)

  def get_product_price(self):
    price_lbl = self.get_text(CheckoutOverviewLocator.TOTAL_ITEM_PRICE_LABEL)
    price = Utils.convert_string_to_float(self, price_lbl)
    return float(price)

  def get_tax(self):
    tax_lbl = self.get_text(CheckoutOverviewLocator.TAX_LABEL)
    tax = Utils.convert_string_to_float(self, tax_lbl)
    return float(tax)

  def get_total_price(self):
    total_price_lbl = self.get_text(CheckoutOverviewLocator.TOTAL_PRICE_LABEL)
    total_price = Utils.convert_string_to_float(self, total_price_lbl)
    return float(total_price)

  def click_finish_button(self):
    return self.click(CheckoutOverviewLocator.FINISH_BUTTON)
