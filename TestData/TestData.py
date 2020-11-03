import json

from Objects.product import Product


def get_account():
  accounts = []
  with open(TestData.ACC_FILE) as acc_json_file:
    data = json.load(acc_json_file)
    for acc in data['user']:
      user = (acc['username'], acc['password'])
      accounts.append(user)


class TestData:
  BASEURL = "https://www.saucedemo.com/index.html"
  BROWSER = "Firefox"
  USERNAME = "standard_user"
  USERNAME1 = "locked_out_user"
  USERNAME2 = "problem_user"
  USERNAME3 = "performance_glitch_user"
  PASSWORD = "secret_sauce"
  ACC_FILE = "TestData/list_account.json"
  FILE = "TestData/testdata.json"

  def getProducts(self):
    products = []
    with open(TestData.FILE) as json_data_file:
      data = json.load(json_data_file)
      for product in data['product']:
        product = Product(product['name'], product['description'], product['price'])
        products.append(product)
      json_data_file.close()
    return products
