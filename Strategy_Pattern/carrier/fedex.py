from carrier.abs_carrier import AbsCarrier


class Fedex(AbsCarrier):
    def cost_of_shipping(self):
        return "£35"

    def __str__(self):
        return "Fedex"