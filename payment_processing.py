# Payment Methods

class CreditCard:
    def pay(self, amount):
        print("₹", amount, "paid using Credit Card")


class PayPal:
    def pay(self, amount):
        print("₹", amount, "paid using PayPal")


class UPI:
    def pay(self, amount):
        print("₹", amount, "paid using UPI")


class NetBanking:
    def pay(self, amount):
        print("₹", amount, "paid using Net Banking")


class Cryptocurrency:
    def pay(self, amount):
        print("₹", amount, "paid using Cryptocurrency")


# Payment Processor
class PaymentProcessor:
    def __init__(self):
        self.balance = 5000   # Initial Balance

    def process(self, payment_method, amount):
        if amount <= self.balance:
            payment_method.pay(amount)
            self.balance -= amount
            print("Payment Successful!")
            print("Remaining Balance: ₹", self.balance)
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print("Current Balance: ₹", self.balance)


# Main Program
processor = PaymentProcessor()

while True:
    print("\n=== PAYMENT SYSTEM ===")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. UPI")
    print("4. Net Banking")
    print("5. Cryptocurrency")
    print("6. Check Balance")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = int(input("Enter Amount: "))
        processor.process(CreditCard(), amount)

    elif choice == 2:
        amount = int(input("Enter Amount: "))
        processor.process(PayPal(), amount)

    elif choice == 3:
        amount = int(input("Enter Amount: "))
        processor.process(UPI(), amount)

    elif choice == 4:
        amount = int(input("Enter Amount: "))
        processor.process(NetBanking(), amount)

    elif choice == 5:
        amount = int(input("Enter Amount: "))
        processor.process(Cryptocurrency(), amount)

    elif choice == 6:
        processor.check_balance()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")