from Locators.checkout_information_locator import CheckoutInforLocator
from Objects.checkoutinfo import CheckoutInfo
from Pages.base_page_object import BasePage


class CheckoutInfoPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)

  def input_checkout_info(self, firstname, lastname, postalcode):
    self.enter_text(CheckoutInforLocator.FIRSTNAME_TEXTBOX, firstname)
    self.enter_text(CheckoutInforLocator.LASTNAME_TEXTBOX, lastname)
    self.enter_text(CheckoutInforLocator.POSTALCODE_TEXTBOX, postalcode)

  def click_continue_button(self):
    self.click(CheckoutInforLocator.CONTINUE_BTN)

  def click_cancel_button(self):
    self.click(CheckoutInforLocator.CANCEL_BTN)
