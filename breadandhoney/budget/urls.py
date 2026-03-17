from django.urls import path
from . import views
from budget.forms import Quiz1Form, Quiz2Form
from budget.views import BudgetWizard

urlpatterns = [
    path("",views.index, name="index"),
    path("quiz/", BudgetWizard.as_view([Quiz1Form, Quiz2Form]), name='budget-quiz'),
    path("quiz/end", views.quiz_end, name='quiz-end')
]