class Sweet:
    def __init__(self, sweet_id, name, category, price, quantity):
        self.id = sweet_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

class SweetShop:
    def __init__(self):
        self.inventory = {}

    def add_sweet(self, sweet):
        self.inventory[sweet.id] = sweet
