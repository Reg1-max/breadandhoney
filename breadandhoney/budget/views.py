from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Income, Outgoings
from formtools.wizard.views import SessionWizardView

# Create your views here.
def index(request):
    try:
        budgetin = Income.objects.last()
        budgetout = Outgoings.objects.last()
        leftover = budgetin.total() - budgetout.total()
        if budgetin == None and budgetout == None:
            budgetin = False
            budgetout = False
            leftover = False
            return render(request, "budget/index.html",{"budgetin":budgetin, "budgetout":budgetout, "leftover":leftover})
    except (Income.DoesNotExist, Outgoings.DoesNotExist):
        budgetin = False
        budgetout = False
        leftover = False
    return render(request, "budget/index.html",{"budgetin":budgetin, "budgetout":budgetout, "leftover":leftover})

def quiz_end(request):
    return render(request, "budget\quizend.html")

class BudgetWizard(SessionWizardView):
    
    def done(self, form_list, form_dict):
        income = Income()
        income.salary = self.get_form_step_data(form_list[0])['0-salary']
        income.bonus = self.get_form_step_data(form_list[0])['0-bonus']
        income.other = self.get_form_step_data(form_list[0])['0-other']
        income.save()

        outgoings = Outgoings()
        outgoings.accom = self.get_form_step_data(form_list[1])['1-accom']
        outgoings.utilities = self.get_form_step_data(form_list[1])['1-utilities']
        outgoings.travel = self.get_form_step_data(form_list[1])['1-travel']
        outgoings.groceries = self.get_form_step_data(form_list[1])['1-groceries']
        outgoings.entertainment = self.get_form_step_data(form_list[1])['1-entertainment']
        outgoings.other = self.get_form_step_data(form_list[1])['1-other']
        outgoings.save()

        return HttpResponseRedirect("end")