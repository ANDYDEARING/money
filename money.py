class DifferentCurrencyError(Exception):
    pass


class Currency:
    """
    Represents a currency. Does not contain any exchange rate info.
    """

    def __init__(self, name, code, symbol=None, digits=2):
        """
        Parameters:
        - name -- the English name of the currency
        - code -- the ISO 4217 three-letter code for the currency
        - symbol - optional symbol used to designate currency
        - digits -- number of significant digits used
        """
        self.name = name
        self.code = code
        self.symbol = symbol
        self.digits = digits

    def __str__(self):
        """
        Should return the currency code, or code with symbol in parentheses.
        """
        if self.symbol is None:
            return self.code
        else:
            return f"({self.symbol})"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.name == other.name and
                self.code == other.code and self.symbol == other.symbol and
                self.digits == other.digits)


class Money:
    """
    Represents an amount of money. Requires an amount and a currency.
    """

    def __init__(self, amount, currency):
        """
        Parameters:
        - amount -- quantity of currency
        - currency -- type of currency
        """
        self.amount = amount
        self.currency = currency

    def __str__(self):
        """
        Should use the currency symbol if available, else use the code.
        Use the currency digits to determine number of digits to show.
        """
        if self.currency.symbol is not None:
            return f"{self.currency.symbol}{self.amount:.{self.currency.digits}f}"
        else:
            return f"{self.currency.code} {self.amount:.{self.currency.digits}f}"

    def __repr__(self):
        return f"<Money {str(self)}>"

    def __eq__(self, other):
        """
        All fields must be equal to for the objects to be equal.
        """
        return (type(self) == type(other) and self.amount == other.amount and
                self.currency == other.currency)

    def add(self, other):
        """
        Add two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency != other.currency:
            raise DifferentCurrencyError
        else:
            new_money = Money(self.amount+other.amount, self.currency)
            return new_money

    def sub(self, other):
        """
        Subtract two money objects of the same currency. If they have different
        currencies, raise a DifferentCurrencyError.
        """
        if self.currency != other.currency:
            raise DifferentCurrencyError
        else:
            new_money = Money(self.amount-other.amount, self.currency)
            return new_money

    def mul(self, multiplier):
        """
        Multiply a money object by a number to get a new money object.
        """
        new_money = Money(self.amount*multiplier, self.currency)
        return new_money

    def div(self, divisor):
        """
        Divide a money object by a number to get a new money object.
        """
        new_money = Money(self.amount/divisor, self.currency)
        return new_money
    
    def __add__(self,other):
        """allows use of the + operand between Money objects"""
        return self.add(other)

    def __sub__(self,other):
        """allows use of the - operand between Money objects"""
        return self.sub(other)

    def __mul__(self,multiplier):
        """allows use of the * operand between a Money object and number"""
        return self.mul(multiplier)

    def __truediv__(self,divisor):
        """allows use of the / operand between a Money object and an int"""
        return self.div(divisor)
