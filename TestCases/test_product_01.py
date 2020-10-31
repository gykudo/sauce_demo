import sys

sys.path.append(".")
import unittest
from TestCases.base_test import BaseTest
from Pages.products_page import ProductsPage
from TestData.TestData import TestData
from Utils.assertion import Assertion


class TestProduct01(BaseTest):

  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  def test_product_display_correctly(self):
    products_page = ProductsPage(self.driver)
    products = TestData.getProducts()

    for index, expected_product in enumerate(products, start=1):
      ###Check add/remove button existed, if existed click add/remove button###
      self.assertTrue(products_page.does_add_button_exist(index))
      products_page.add_product_to_cart(index)
      self.assertEqual(1, products_page.get_product_badge())
      self.assertTrue(products_page.does_remove_button_exist(index))

      products_page.remove_product_from_cart(index)
      self.assertEqual(0, products_page.get_product_badge())
      self.assertTrue(products_page.is_product_badge_invisible())

      actual_product = products_page.get_product_info(index)
      assertion = Assertion()
      assertion.compare_product_info(actual_product, expected_product)


if __name__ == "__main__":
  unittest.main()
