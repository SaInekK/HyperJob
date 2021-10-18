from django.contrib.auth.views import LoginView
# Create your views here.
from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from .models import Resume
from .forms import *

from django.contrib.auth.models import User


class MenuView(View):
    template_name = 'menu.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ResumesView(View):
    template_name = 'resumes.html'
    # vacansies = Vacansies.objects.all()
    # model = Vacansies

    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, self.template_name, {'resumes': resumes})


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login')
        if not request.user.is_staff:
            return redirect('/resume/new')
        else:
            return redirect('/vacancy/new')
        return render(request, 'profile.html')


class AddResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'create_resume.html')

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.is_staff:
            return HttpResponse(status=403)

        else:
            Resume.objects.create(author=request.user, description=request.POST.get('description'))
            return redirect('/home')

