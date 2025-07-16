import unittest
from sweetshop import Sweet, SweetShop

class TestSweetShop(unittest.TestCase):

    def setUp(self):
        self.shop = SweetShop()

    def test_add_sweet(self):
        sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        self.shop.add_sweet(sweet)
        self.assertIn(1001, self.shop.inventory)

    def test_delete_sweet(self):
        sweet = Sweet(1002, "Gulab Jamun", "Milk-Based", 10, 50)
        self.shop.add_sweet(sweet)
        self.shop.delete_sweet(1002)
        self.assertNotIn(1002, self.shop.inventory)

    def test_view_sweets(self):
        sweet1 = Sweet(1003, "Gajar Halwa", "Vegetable-Based", 30, 15)
        sweet2 = Sweet(1004, "Rasgulla", "Milk-Based", 12, 25)
        self.shop.add_sweet(sweet1)
        self.shop.add_sweet(sweet2)
        all_sweets = self.shop.view_sweets()
        self.assertEqual(len(all_sweets), 2)

if __name__ == '__main__':
    unittest.main()
