
class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """Credit a new credit card instance.

        The initial balance is zero.

        customer  the name of the customer (e.g.,'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the account identifier (e.g.,'5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        balance   current balance, default 0
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

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
        if not isinstance(price, (int, float)):    # error checking
            raise TypeError('price must be numeric.')
        elif price < 0:
            raise ValueError('price cannot be negative.')

        if price + self._balance > self._limit:    # if charge would exceed limit
            return False                           # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        if not isinstance(amount, (int, float)):   # error checking
            raise TypeError('amount must be numeric.')
        elif amount < 0:
            raise ValueError("amount cannot be negative.")

        self._balance -= amount


if __name__ == '__main__':
    cc = CreditCard("yw", "bank of China", '1234 5678 9900', 5000)
    print('Error checking: change("123")')
    cc.charge('123')
