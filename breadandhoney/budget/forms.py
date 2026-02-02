from django import forms

class Quiz1Form(forms.Form):
    salary = forms.CharField(label="salary")
    bonus = forms.CharField(label="bonus")
    other = forms.CharField(label="other")

class Quiz2Form(forms.Form):
    accom = forms.CharField(label="Accommodation")
    utilities = forms.CharField(label="Utilities")
    travel = forms.CharField(label="Travel")
    groceries = forms.CharField(label="Groceries")
    entertainment = forms.CharField(label="Entertainment")
    other = forms.CharField(label="Other")