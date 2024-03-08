from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        print("POST received")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Form validated")
            form.save()
            return redirect("/create/success/")
    else:
        form = UserCreationForm()
        
    return render(request, "register/register.html", {"form":form})