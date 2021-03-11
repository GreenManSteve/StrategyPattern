from products import *
from shipping import Shipping_Cost

prod = CD()
shipping = Shipping_Cost(prod)
cost = shipping.get_shipping_cost()
print(cost)