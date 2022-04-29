class VendingMachine:
    def __init__(self, num_items, item_price):
        self.numItems = num_items
        self.itemPrice = item_price

    def buy(self, req_items, money):

        if req_items > self.numItems:
            return "item not available"

        change = money - (req_items * self.itemPrice)
        totalPrice = req_items * self.itemPrice

        if totalPrice > money:
            return "Not enough money"

        self.numItems -= req_items
        return change

    pass


# Custom Test
vend = VendingMachine(1400, 2)
arrItemReq = [120, 50, 20, 30, 20, 40, 11]
arrMoney = [170, 125, 75, 32, 59, 140, 85]
expenses = 0

for i in range(len(arrItemReq)):
    result = vend.buy(arrItemReq[i], arrMoney[i])
    if type(result) is int:
        expenses += result

print(f"Your expense : {expenses}")
