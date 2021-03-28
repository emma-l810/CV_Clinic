from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .forms import Form

# Create your views here.
def index(request):
    context = {}
    return render(request, 'polls/index.html', context)
    # return HttpResponse("this is views.py in polls")

def registration(request):
    form = Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {"form": form,}
    return render(request, 'polls/registration.html', context)

def login(request):
    context = {}
    return render(request, 'polls/login.html', context)

def profile(request):
    context = {}
    return render(request, 'polls/profile.html', context)
