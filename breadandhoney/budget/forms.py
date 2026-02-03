from django import forms

class Quiz1Form(forms.Form):
    salary = forms.DecimalField(label="salary",max_digits=11,decimal_places=2)
    bonus = forms.DecimalField(label="bonus",max_digits=11,decimal_places=2)
    other = forms.DecimalField(label="other",max_digits=11,decimal_places=2)

class Quiz2Form(forms.Form):
    accom = forms.DecimalField(label="Accommodation",max_digits=11,decimal_places=2)
    utilities = forms.DecimalField(label="Utilities",max_digits=11,decimal_places=2)
    travel = forms.DecimalField(label="Travel",max_digits=11,decimal_places=2)
    groceries = forms.DecimalField(label="Groceries",max_digits=11,decimal_places=2)
    entertainment = forms.DecimalField(label="Entertainment",max_digits=11,decimal_places=2)
    other = forms.DecimalField(label="Other",max_digits=11,decimal_places=2)