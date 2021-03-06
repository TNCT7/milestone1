class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    #@classmethod
    #def from_sum(cls, value1, value2):
    #    return cls(value1 + value2)

    @staticmethod
    def from_sum( value1, value2):
        return FixedFloat(value1 + value2)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

"""
When we now call:

* `Euro.from_sum()`, `cls` is the `Euro` class.
* `FixedFloat.from_sum()`, `cls` is the `FixedFloat` class.
"""

print(Euro.from_sum(16.7565, 90))  # <Euro €106.75>