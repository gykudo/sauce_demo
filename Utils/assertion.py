import unittest
import logging



class Assertion(unittest.TestCase):
  def compare_product_info(self, actual_product, expected_product):
    msg = "Actual: '{}', Expected: '{}'"
    try:
      self.assertEqual(actual_product.name, expected_product.name)
    except AssertionError:
      logging.error(msg.format(actual_product.name, expected_product.name))

    try:
      self.assertEqual(actual_product.description, expected_product.description)
    except AssertionError:
      logging.error(msg.format(actual_product.description, expected_product.description))

    try:
      self.assertEqual(actual_product.price, expected_product.price)
    except AssertionError:
      logging.error(msg.format(actual_product.price, expected_product.price))



