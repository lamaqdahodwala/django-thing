from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import Userform

# Create your views here.

def index(req):
    return render(req, 'index.html')

def signup(req):
    if req.method == 'POST':
        form = Userform(req.POST or None)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('bro u dunce')
    return render(req, 'signup.html')