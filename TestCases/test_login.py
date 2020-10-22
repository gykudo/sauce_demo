import sys

sys.path.append(".")
import unittest
from TestCases.base_test import BaseTest
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from TestData.TestData import TestData
from Objects.account import Account


class TestLogin(BaseTest):

  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  #@unittest.SkipTest
  def test_login_lockout_account(self):
    login_page = LoginPage(self.driver)
    account = Account(TestData.USERNAME1, TestData.PASSWORD)
    login_page.login(account)
    self.assertIn("Sorry, this user has been locked out.", login_page.get_message())

  @unittest.SkipTest
  def test_login_performance_account(self):
    login_page = LoginPage(self.driver)
    account = Account(TestData.USERNAME3, TestData.PASSWORD)
    login_page.login(account)
    product_item = ProductPage(self.driver)
    product_item.check_product_existed()

  @unittest.SkipTest
  def test_login_problem_account(self):
    login_page = LoginPage(self.driver)
    account = Account(TestData.USERNAME2, TestData.PASSWORD)
    login_page.login(account)
    product_item = ProductPage(self.driver)
    product_item.check_product_existed()

  def test_login_standard_account(self):
    login_page = LoginPage(self.driver)
    account = Account(TestData.USERNAME, TestData.PASSWORD)
    login_page.login(account)
    product_item = ProductPage(self.driver)
    product_item.check_product_existed()


if __name__ == "__main__":
  unittest.main()
