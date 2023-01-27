from django.shortcuts import render
from .forms import SignUpForm
from .models import *

# Create your views here.
def vedic(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
       fm = SignUpForm()
    allq = Quiz.objects.all()
    topic = Topic.objects.all()
    return render(request,'home.html',{"allq":allq,"topic":topic,"form":fm})