import unittest
from sweetshop import Sweet, SweetShop

class TestSweetShop(unittest.TestCase):
    def setUp(self):
        self.shop = SweetShop()

    def test_add_sweet(self):
        sweet = Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20)
        self.shop.add_sweet(sweet)
        self.assertIn(1001, self.shop.inventory)

if __name__ == '__main__':
    unittest.main()
