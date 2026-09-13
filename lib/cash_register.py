#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount.")

    def add_item(self, item, price, quantity=1):
        cost = price * quantity
        self.total += cost
        
        # Append item for each unit in quantity so multiples are recorded
        for _ in range(quantity):
            self.items.append(item)
            
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return self.total

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        return self.total

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last_tx = self.previous_transactions.pop()
        item = last_tx["item"]
        quantity = last_tx["quantity"]
        cost = last_tx["price"] * quantity

        self.total -= cost
        for _ in range(quantity):
            if item in self.items:
                self.items.remove(item)