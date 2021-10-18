from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from .models import Vacancy
from .forms import *

from django.contrib.auth.models import User


class VacanciesView(View):
    template_name = 'vacancies.html'
    # vacansies = Vacancy.objects.all()
    # model = Vacansies

    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, self.template_name, {'vacancies': vacancies})
    #
    # def get_queryset(self):
    #     return Vacansies.objects.all()


class AddVacancyView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'create_vacancy.html')

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponse(status=403)

        else:
            Vacancy.objects.create(author=request.user, description=request.POST.get('description'))
            return redirect('/home')
