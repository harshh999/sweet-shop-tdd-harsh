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

    def delete_sweet(self, sweet_id):
        if sweet_id in self.inventory:
            del self.inventory[sweet_id]

    def view_sweets(self):
        return list(self.inventory.values())
