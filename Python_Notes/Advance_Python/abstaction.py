from abc import ABC, abstractmethod

# Abstraction: define a common interface without exposing implementation details.
# Concrete subclasses provide specific behavior while users work with the abstract type.

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def pay(self):
        print("processing credit card payment")

class PayPalPayment(Payment):
    def pay(self):
        print("processing PayPal payment")

# Example usage:
# payment = CreditCardPayment()
# payment.pay()
# payment = PayPalPayment()
# payment.pay()
