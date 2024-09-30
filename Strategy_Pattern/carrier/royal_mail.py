from carrier.abs_carrier import AbsCarrier


class RoyalMail(AbsCarrier):
    def cost_of_shipping(self):
        return "£10"

    def __str__(self):
        return "Royal Mail"