from django.test import TestCase
from budget.models import Income

class IncomeTestCase(TestCase):
    def setUp(self):
        self.income = Income.objects.create(
            salary=5000,
            bonus=1500,
            other=200
        )

    def test_total(self):
        """Test total income calculation"""
        expected_total = self.income.salary + self.income.bonus + self.income.other
        self.assertEqual(self.income.total(),expected_total)
