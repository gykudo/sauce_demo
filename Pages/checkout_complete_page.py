from Locators.checkout_complete_locator import CheckoutCompleteLocator
from Pages.base_page_object import BasePage


class CheckoutCompletePage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)

  def get_complete_message(self):
    complete_msg = self.get_text(CheckoutCompleteLocator.COMPLETE_LABBEL)
    return complete_msg

  def get_pony_image(self):
    pony_img = self.get_elements_size(CheckoutCompleteLocator.PONY_IMAGE)
    return pony_img
