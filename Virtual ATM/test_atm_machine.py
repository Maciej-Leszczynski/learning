import unittest
from atm_machine import Atm, Customer


class TestVirtualAtmMachine(unittest.TestCase):
    def test_customer_instances(self):
        maciek = Customer("Maciek", "1234")
        self.assertIsInstance(maciek, Customer)

    def test_not_customer_instances(self):
        self.assertNotIsInstance(Atm, Customer)

    def test_invalid_pin_number_not_decimal(self):
        with self.assertRaises(ValueError):
            user = Customer("Adam", "Małysz")

    def test_pin_len_not_4(self):
        with self.assertRaises(ValueError):
            user2 = Customer("Kamil", "12345")
            
    def test_pin_is_a_string(self):
        with self.assertRaises(TypeError):
            user3 = Customer("Kamil", 1234)

    def test_balance_of_the_account(self):
        maciek = Customer("Maciek", "1234")
        maciek.log_in("1234")
        self.assertEqual(maciek.check_balance(), "Your current balance is 0.")

    def test_login_function(self):
        ania = Customer("Ania", "1234")
        self.assertEqual(ania.check_balance(), "You must to log in.")
        self.assertFalse(ania.loged)
        ania.log_in("1234")
        self.assertEqual(ania.check_balance(), "Your current balance is 0.")
        self.assertTrue(ania.loged)

    def test_deposit_method(self):
        user4 = Customer("User", "1234")
        user4.log_in("1234")
        user4.deposit(100)
        self.assertEqual(user4.balance, 100)
        with self.assertRaises(ValueError):
            user4.deposit(1001)
            user4.deposit(-1)

    def test_withdraw_method(self):
        user5 = Customer("User", "1234")
        user5.log_in("1234")
        with self.assertRaises(ValueError):
            user5.withdrawal(100)
        user5.deposit(1000)
        user5.withdrawal(50)
        with self.assertRaises(ValueError):
            user5.withdrawal(501)          

if __name__ == "__main__":
    unittest.main()
