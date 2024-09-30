from carrier import Fedex
from carrier import RoyalMail
from shipping.shipper import Shipper

# carrier can be set to an instance of Fedex or RoyalMail

carrier = Fedex()
shipper = Shipper(carrier)
price = shipper.get_cost()
print("The cost of shipping via {} is {}".format(carrier.__str__(), price))