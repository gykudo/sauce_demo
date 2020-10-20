import sys
import unittest
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from TestData.TestData import TestData

sys.path.append(".")


class BaseTest(unittest.TestCase):

  @classmethod
  def setUp(self):
    browser = self.get_browser()
    self.driver = self.startBrowser(browser)
    self.driver.maximize_window()

  @classmethod
  def tearDown(self):
    try:
      self.driver.close()
      self.driver.quit()
    except Exception as msg:
      print("message: %s" % str(msg))
      pass

  def startBrowser(name="chrome"):
    """
    browsers，"firefox"、"chrome"、"ie"、"phantomjs"
    """
    try:
      if name.lower() == "firefox" or name.lower() == "ff":
        print("start browser name :Firefox")
        # return webdriver.Firefox(executable_path='')
        return webdriver.Firefox()
      elif name.lower() == "chrome":
        print("start browser name :Chrome")
        return webdriver.Chrome()
      elif name.lower() == "edge":
        print("start browser name :Edge")
        return webdriver.MicrosoftEdge()
      elif name.lower() == "phantomjs":
        print("start browser name :phantomjs")
        return webdriver.PhantomJS()
      else:
        print("Not found this browser,You can use ‘firefox‘, ‘chrome‘, ‘ie‘ or ‘phantomjs‘")
    except Exception as msg:
      print("message: %s" % str(msg))

  def get_browser():
    try:
      return os.environ['BROWSER']
    except KeyError:
      return TestData.BROWSER
