from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Quiz1Form, Quiz2Form
from .models import Income, Outgoings

# Create your views here.
def index(request):
    try:
        budgetin = Income.objects.last()
        budgetout = Outgoings.objects.last()
        leftover = budgetin.total() - budgetout.total()
    except (Income.DoesNotExist, Outgoings.DoesNotExist):
        budgetin = False
        budgetout = False
        leftover = False
    return render(request, "budget/index.html",{"budgetin":budgetin, "budgetout":budgetout, "leftover":leftover})

def quiz_1(request):
    if request.method == "POST":
        form1 = Quiz1Form(request.POST)
        if form1.is_valid():
            income = Income()
            income.salary = form1.data['salary']
            income.bonus = form1.data['bonus']
            income.other = form1.data['other']
            income.save()
            return HttpResponseRedirect("/budget/quiz/2")
    else:
        form1 = Quiz1Form()
    return render(request, "budget\quiz1.html", {"form":form1})

def quiz_2(request):
    if request.method == "POST":
        form2 = Quiz2Form(request.POST)
        if form2.is_valid():
            outgoings = Outgoings()
            outgoings.accom = form2.data['accom']
            outgoings.utilities = form2.data['utilities']
            outgoings.travel = form2.data['travel']
            outgoings.groceries = form2.data['groceries']
            outgoings.entertainment = form2.data['entertainment']
            outgoings.other = form2.data['other']
            outgoings.save()
            return HttpResponseRedirect("/budget/quiz/end")
    else:
        form2 = Quiz2Form()
    return render(request, "budget\quiz2.html", {"form":form2})

def quiz_end(request):
    return render(request, "budget\quizend.html")