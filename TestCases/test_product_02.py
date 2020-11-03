import sys
import unittest
import os

sys.path.append(".")

from TestCases.base_test import BaseTest
from Pages.products_page import ProductsPage
from Pages.cart_page import CartPage
from Pages.checkout_info_page import CheckoutInfoPage
from TestData.TestData import TestData
from Utils.assertion import Assertion
from Pages.login_page import LoginPage



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

    cart_page = CartPage(self.driver)
    for index in [1, 2, 3]:
      actual_product = cart_page.get_product_info(index)
      expected_product = products[index - 1]
      assertion = Assertion()
      assertion.compare_product_info(actual_product, expected_product)

    cart_page.click_checkout_button()
    checkout_info_page = CheckoutInfoPage(self.driver)
    checkout_info_page.input_checkout_info('Ryan', 'Tu', '700000')
    checkout_info_page.click_continue_button()

if __name__ == "__main__":
  unittest.main()
