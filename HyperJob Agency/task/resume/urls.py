from django.urls import path
from django.views.generic import RedirectView

from .views import *
from .forms import *

urlpatterns = [
    path('', MenuView.as_view()),
    path('resumes/', ResumesView.as_view()),
    path('login', MyLoginView.as_view()),
    # path('logout', LogoutView.as_view()),
    path('signup', MySignupView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('home', ProfileView.as_view()),
    path('home/', RedirectView.as_view(url='/home')),
    path('resume/new', AddResumeView.as_view()),
]