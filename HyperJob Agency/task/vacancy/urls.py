from django.urls import path

from .views import *

urlpatterns = [
    path('vacancies/', VacanciesView.as_view()),
    path('vacancy/new', AddVacancyView.as_view()),
]