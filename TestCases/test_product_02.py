import sys
import unittest

sys.path.append(".")

from TestCases.base_test import BaseTest
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from Pages.cart_page import CartPage
from Pages.checkout_info_page import CheckoutInfoPage
from Pages.checkout_overview_page import CheckoutOverViewPage
from Pages.checkout_complete_page import CheckoutCompletePage
from TestData.TestData import TestData
from Utils.assertion import Assertion



class TestProduct02(BaseTest):

  def setUp(self):
    super().setUp()
    login_page = LoginPage(self.driver)
    login_page.login(TestData.USERNAME, TestData.PASSWORD)

  def tearDown(self):
    super().tearDown()

  def test_product_display_correctly(self):

    products_page = ProductsPage(self.driver)
    products = TestData.getProducts(self)
    for index in [2, 4, 6]:
      products_page.add_product_to_cart(index)
    products_page.click_product_cart()
    assertion = Assertion()
  ## Compare selected product information in cart page, caculate total price of selected product
    prices = []
    cart_page = CartPage(self.driver)
    for index in [1, 2, 3]:
      actual_product = cart_page.get_product_info(index)
      expected_product = products[index - 1]
      assertion.compare_product_info(actual_product, expected_product)
      price = cart_page.get_price(index)
      prices.append(price)
    total_price = sum(prices)
    est_tax = float("{:.2f}".format(total_price * 0.08))
    mess = "Estimate price is '%s'" % (total_price)
    print(mess)
    est_total_price = total_price + est_tax

  # Transit to checkout infor page
    cart_page.click_checkout_button()
    checkout_info_page = CheckoutInfoPage(self.driver)
    checkout_info_page.input_checkout_info('Ryan', 'Tu', '700000')
    checkout_info_page.click_continue_button()

  ## Transit to Checkout Overview Page, compare selected product in the checkout overview page
    checkout_over = CheckoutOverViewPage(self.driver)
    for index in [1, 2, 3]:
      actual_product = checkout_over.get_product_overview_info(index)
      expected_product = products[index - 1]
      assertion.compare_product_info(actual_product, expected_product)
    actual_price = checkout_over.get_product_price()
    actual_tax = checkout_over.get_tax()
    actual_total_price = checkout_over.get_total_price()
    self.assertEqual(actual_price, total_price)
    self.assertEqual(actual_tax, est_tax)
    self.assertEqual(actual_total_price, est_total_price)

  # Transit to checkout complete page
    checkout_over.click_finish_button()
    checkout_complete = CheckoutCompletePage(self.driver)
    complete_msg = checkout_complete.get_complete_message()
    self.assertIn('Your order has been dispatched, and will arrive just as fast as the pony can get there!', complete_msg)



if __name__ == "__main__":
  unittest.main()
