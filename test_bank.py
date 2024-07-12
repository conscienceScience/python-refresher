import unittest
import bank
import numpy as np


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = bank.Bank("Mr.Goose", "12345")
    
    def test_object(self):
        self.assertEqual(self.bank.get_name(), "Mr.Goose")
        self.assertNotEqual(self.bank.get_name(), "Mr.Dog")
        self.assertEqual(self.bank.get_acc_num(), "12345")
        self.assertNotEqual(self.bank.get_acc_num(), 12345)
        self.assertNotEqual(self.bank.get_acc_num(), "23556")

    def test_deposit(self):
        self.assertEqual(self.bank.deposit(500),500)
        self.assertNotEqual(self.bank.deposit(500),500)        

    def test_withdraw(self):
        self.assertEqual(self.bank.withdraw(-500),'error')
        self.assertNotEqual(self.bank.withdraw(500),1000) 
        self.assertEqual(self.bank.deposit(500),500) 
        self.assertEqual(self.bank.withdraw(500),0)      


    def test_print_current_balance(self):
        self.assertEqual(self.bank.print_current_balance(),0)
        self.assertNotEqual(self.bank.deposit(500),1500)        

