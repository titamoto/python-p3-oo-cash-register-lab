#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.transactions = []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.transactions.append(price * quantity)
    count = 1
    while count <= quantity:
      self.items.append(title)
      count += 1

  def apply_discount(self):
    self.total -= self.total * self.discount / 100
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= self.transactions[-1]