from django.db import models

# Create your models here.
class Income(models.Model):
    incomeID = models.BigAutoField(primary_key=True)
    salary = models.DecimalField(decimal_places=2, max_digits=11)
    bonus = models.DecimalField(decimal_places=2, max_digits=11)
    other = models.DecimalField(decimal_places=2, max_digits=11)
    def total(self):
        return self.salary + self.bonus + self.other

class Outgoings(models.Model):
    outID = models.BigAutoField(primary_key=True)
    accom = models.DecimalField("Accommodation", max_digits=11, decimal_places=2)
    utilities = models.DecimalField(decimal_places=2, max_digits=11)
    travel = models.DecimalField(decimal_places=2, max_digits=11)
    groceries = models.DecimalField(decimal_places=2, max_digits=11)
    entertainment = models.DecimalField(decimal_places=2, max_digits=11)
    other = models.DecimalField(decimal_places=2, max_digits=11)
    def total(self):
        return self.accom + self.utilities + self.travel + self.groceries + self.entertainment + self.other