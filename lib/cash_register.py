class Checkout:
    def __init__(self, promo=0):
        self.promo = promo
        self.amount_due = 0
        self.product_list = []
        self.previous_transaction = 0

    def add_product(self, name, cost, quantity=1):
        self.amount_due += cost * quantity
        self.product_list.extend([name] * quantity)
        self.previous_transaction = cost * quantity

    def apply_promo(self):
        if self.promo > 0:
            promo_amount = self.amount_due * (self.promo / 100)
            self.amount_due -= promo_amount
            return f"After the promotion, the total comes to ${self.amount_due:.2f}."
        else:
            return "There is no promotion to apply."

    def undo_last_transaction(self):
        self.amount_due -= self.previous_transaction
