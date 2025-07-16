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

    def test_search_by_name(self):
        self.shop.add_sweet(Sweet(1005, "Kaju Katli", "Nut-Based", 50, 20))
        self.shop.add_sweet(Sweet(1006, "Besan Ladoo", "Flour-Based", 25, 10))
        results = self.shop.search_by_name("kaju")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Kaju Katli")

if __name__ == '__main__':
    unittest.main()
