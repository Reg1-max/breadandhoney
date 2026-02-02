from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("quiz/1", views.quiz_1, name="budget-quiz-1"),
    path("quiz/2", views.quiz_2, name="budget-quiz-2"),
    path("quiz/end", views.quiz_end, name="budget-quiz-end")
]