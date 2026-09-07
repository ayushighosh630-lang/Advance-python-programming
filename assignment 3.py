
class CreditCardPayment:
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


class PayPalPayment:
    def pay(self, amount):
        print("Paid ₹", amount, "using PayPal")


class BitcoinPayment:
    def pay(self, amount):
        print("Paid ₹", amount, "using Bitcoin")


class PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def make_payment(self, amount):
        self.payment_method.pay(amount)


print("Payment Processing System")
print("-------------------------")
print("1. Credit Card")
print("2. PayPal")
print("3. Bitcoin")

choice = int(input("Enter your choice: "))
amount = float(input("Enter amount to pay: ₹"))

if choice == 1:
    payment = CreditCardPayment()

elif choice == 2:
    payment = PayPalPayment()

elif choice == 3:
    payment = BitcoinPayment()

else:
    print("Invalid choice")
    exit()

processor = PaymentProcessor(payment)
processor.make_payment(amount)