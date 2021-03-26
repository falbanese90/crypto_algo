"""Retrieves Technical analysis and creates Class."""

class Technicals():
    """Create attributes based on technical analysis."""

    def __init__(self, df):
        """Price and sma50 attributes."""
        self.price = df['open'][-1]
        self.fifty = df['sma_50'][-1]

    @property
    def percent_over_fifty(self):
        """Grab the percentage over 50 day MA."""
        return round((((self.price - self.fifty) / self.price) * 100), 2)

    @property
    def sell(self):
        return self.percent_over_fifty > 40

    def __str__(self):
        """String Representation"""
        return (f'Price: {self.price}, 50-Day: {self.fifty}'
                f', Percent Over: {self.percent_over_fifty}')
