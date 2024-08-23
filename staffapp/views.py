from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def stafflogin(request):
    if request.method == 'POST':
        fname  = request.POST.get('fname')
        lname = request.POST.get('l')