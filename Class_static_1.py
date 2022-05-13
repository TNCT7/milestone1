class FixedFloat:
    def __init__(self,amount):
        self.amount = amount

    def __repr__(self):
        return f'fixed amount:{self.amount:.2f}'

    #@staticmethod
    #def from_sum(a,b):
     #   return FixedFloat(a+b)

    @classmethod
    def from_sum(cls,a, b):
        return cls(a + b)

# resaon we sused static method becauuse we nned to create object with argument which cannot be used fwd
#ff = FixedFloat(18.74569)
#print(ff.__repr__())

print(FixedFloat.from_sum(10.4533,11.25434))

class Dollars(FixedFloat):
    def __init__(self,amount):
        super().__init__(amount)
        #self.dollar_sign = dollar_sign

    dollar_sign ='$'

    def __repr__(self):
        return f'Dollar val:{self.dollar_sign}{self.amount}'

#d1 = Dollars(16.12544,'$')
#print(d1.__repr__())
print(Dollars.from_sum(35.214,45.234))






