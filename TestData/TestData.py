import json

from Objects.product import Product


class TestData():
  BASEURL = "https://www.saucedemo.com/index.html"
  BROWSER = "Firefox"
  USERNAME = "standard_user"
  USERNAME1 = "locked_out_user"
  USERNAME2 = "problem_user"
  USERNAME3 = "performance_glitch_user"
  PASSWORD = "secret_sauce"
  ACC_FILE = "TestData/list_account.json"
  FILE = "TestData/testdata.json"

  def get_account(self):
    accounts = []
    with open(TestData.ACC_FILE) as acc_json_file:
      data = json.load(acc_json_file)
      for acc in data['user']:
        user = accounts(acc['username'], acc['password'])
        accounts.append(user)

  def getProducts(self):
    products = []
    with open(TestData.FILE) as json_data_file:
      data = json.load(json_data_file)
      for product in data['product']:
        product = Product(product['name'], product['description'], product['price'])
        products.append(product)
    return products


