"""Retrieves Technical analysis and creates Class."""


class Technicals():
    """Create attributes based on technical analysis."""

    def __init__(self, df):
        """Price and sma50 attributes."""
        self.price = df['close'][-1]
        self.fifty = df['sma_50'][-1]

    @property
    def percent_over_fifty(self):
        """Grab the percentage over 50 day MA."""
        return round((((self.price - self.fifty) / self.price) * 100), 2)

    @property
    def sell(self):
        return self.percent_over_fifty >= 40

    def buy(self):
        return self.price <= self.fifty

    def __str__(self):
        """String Representation"""
        if self.sell:
            return "Its time to Sell."
        elif self.buy:
            return "It's time to Buy."
        else:
            return "Patience Pays."
