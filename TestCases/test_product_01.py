import sys
import unittest

sys.path.append(".")

from TestCases.base_test import BaseTest
from Pages.products_page import ProductsPage
from TestData.TestData import TestData
from Utils.assertion import Assertion
from Pages.login_page import LoginPage


class TestProduct01(BaseTest):

  def setUp(self):
    super().setUp()

    login_page = LoginPage(self.driver)
    login_page.login(TestData.USERNAME, TestData.PASSWORD)

  def tearDown(self):
    super().tearDown()

  def test_product_display_correctly(self):
    products_page = ProductsPage(self.driver)
    products = TestData.getProducts(self)

    for index, expected_product in enumerate(products, start=1):
      '''Add & remove all products'''
      products_page.add_product_to_cart(index)
      self.assertTrue(products_page.does_remove_button_exist(index))
      self.assertEqual(1, products_page.get_product_badge())

      products_page.remove_product_from_cart(index)
      self.assertTrue(products_page.does_add_button_exist(index))
      self.assertTrue(products_page.is_product_badge_invisible())

      actual_product = products_page.get_product_info(index)
      assertion = Assertion()
      assertion.compare_product_info(actual_product, expected_product)


if __name__ == "__main__":
  unittest.main()
