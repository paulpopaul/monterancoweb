
from django.conf import settings
from django.shortcuts import redirect, render
from django.template.loader import get_template

def home(request):
    return render(request,'home.html')  