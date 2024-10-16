from bank.ubs import UBS
from investments.call_account import CallAccount
from investments.isa import Isa

# product can be set to Isa(n) or CallAccount(n)

product = Isa(500)
bank = UBS(product)
compound_total = bank.getYearlyCompound
print("The capital and interest after one year in a {} will be {}".format(product, compound_total))
