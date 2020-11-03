class Product():
  def __init__(self, name, description, price, quantity=1):
    self.name = name
    self.description = description
    self.price = price
    self.quantity = quantity

  def __str__(self):
    return "Product name: '%s', Description: '%s', Price: '%s'" % (self.name, self.description, self.price)
