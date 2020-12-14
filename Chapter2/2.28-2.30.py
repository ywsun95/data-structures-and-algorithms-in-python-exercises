class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Credit a new credit card instance.

        The initial balance is zero.

        customer  the name of the customer (e.g.,'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the account identifier (e.g.,'5391 0375 9387 5309)
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:    # if charge would exceed limit
            return False                           # cannot accept charge
        else:
            self._set_balance(self._balance + price)
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._set_balance(self._balance - amount)

    def _set_balance(self, b):
        """Change the balance."""
        self._balance = b


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr, pct):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        customer  the name of the customer (e.g.,'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the account identifier (e.g.,'5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
        pct       a percentage of the balance.
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._count = 0
        self._pct = pct

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)    # call inherited method
        if not success:                    # assess penalty
            self._set_balance(self._balance + 5)
        self._count += 1
        if self._count > 10:
            self._set_balance(self._balance + 1)
        return success                     # caller expects return value

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._set_balance(self._balance * monthly_factor)

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        if amount < self._balance * self._pct:
            self._set_balance(self._balance + 5)
        self._set_balance(self._balance - amount)


if __name__ == '__main__':
    pc = PredatoryCreditCard("yw", "bank of China", '1234 5678 9900', 5000, 0.0825, 0.1)

    print("2.28: additional $1 surcharge.")
    for i in range(12):
        pc.charge(100)
        print(f'No {i+1} change 100, and the balance is', pc.get_balance())

    print()
    print("2.29: if the customer pay the amount less than ")
    print("      10 percentage of the balance. access $5 fee.")
    print("the balance:", pc.get_balance())
    pc.make_payment(100)
    print("after making payment, the balance:", pc.get_balance())


