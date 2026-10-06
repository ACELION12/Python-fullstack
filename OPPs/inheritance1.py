

card_number = input("Enter your card number: ")
card_holder = input("Enter card holder name: ")
amount = float(input("Enter the amount to be paid: "))
class Payment:
    def __init__(self,payment_id, amount):
        self.payment_id = payment_id
        self.amount = 0
    def make_payment(self, amount):
        self.amount += amount
        print(f"Payment of {amount} made. Total amount: {self.amount}Payment ID: {self.payment_id}.Payment successful.")
Payment1 = Payment("P001",100)
Payment2 = Payment("P002",200)
class Creditcarddetails(Payment):
    def __init__(self, payment_id, amount, card_number, card_holder):
        super().__init__(payment_id, amount)
        self.card_number = card_number
        self.card_holder = card_holder
    def display_card_details(self):
        print(f"Card Number: {self.card_number}, Card Holder: {self.card_holder}")
Creditcard1 = Creditcarddetails("P002", 0, card_number, card_holder)
Payment2.make_payment(amount)
Creditcard1.display_card_details()