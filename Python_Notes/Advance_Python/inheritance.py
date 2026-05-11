# Inheritance means a class (child) can use code from another class (parent).
# The child class inherits attributes and methods from the parent class.
# Example: CreditCardPayment and UPIPayment inherit from Payment.

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print("Processing payment of:", self.amount)

class CreditCardPayment(Payment):
    def pay(self):
        print("Processing credit card payment of:", self.amount)

class UPIPayment(Payment):
    def pay(self):
        print("Processing UPI payment of:", self.amount)

# Example usage:
if __name__ == "__main__":
    credit_payment = CreditCardPayment(100)
    credit_payment.pay()

    upi_payment = UPIPayment(200)
    upi_payment.pay()

