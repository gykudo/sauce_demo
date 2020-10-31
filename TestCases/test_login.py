import sys

sys.path.append(".")
import unittest
from TestCases.base_test import BaseTest
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from TestData.TestData import TestData
from Objects.account import Account
from Locators.products_page_locator import ProductPageLocator


class TestLogin(BaseTest):

  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  @unittest.SkipTest
  def test_login_lockout_account(self):
    login_page = LoginPage(self.driver)
    account = Account(TestData.USERNAME1, TestData.PASSWORD)
    login_page.login(account)
    self.assertIn("Sorry, this user has been locked out.", login_page.get_err_message())

  @unittest.SkipTest
  def test_login_performance_account(self):
    login_page = LoginPage(self.driver)
    account = Account(TestData.USERNAME3, TestData.PASSWORD)
    login_page.login(account)
    product_item = ProductsPage(self.driver)
    product_item.check_product_existed()

  @unittest.SkipTest
  def test_login_problem_account(self):
    login_page = LoginPage(self.driver)
    account = Account(TestData.USERNAME2, TestData.PASSWORD)
    login_page.login(account)
    product_item = ProductPage(self.driver)
    print(product_item.get_elements_size(ProductPageLocator.IMG_BROKEN))
    total = product_item.get_broken_img()
    message = "There has '%s' broken images." % (total)
    self.assertEqual(0, total, message)
    product_item.get_product_info(5)

  # @unittest.SkipTest
  def test_login_standard_account(self):
    # with open(list_account.json) as
    login_page = LoginPage(self.driver)
    account = Account(TestData.USERNAME, TestData.PASSWORD)
    login_page.login(account)
    product_page = ProductsPage(self.driver)
    total = product_page.get_broken_img()
    message = "There has '%s' broken images." % total
    self.assertEqual(0, total, message)
    product_list = []
    for i in range(0, 6):
      product_list.append(product_page.get_product_info(1).__str__())
    print(product_list)


if __name__ == "__main__":
  unittest.main()
