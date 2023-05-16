from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

def index(request):
    return render(request, 'index.html')
def sample_inner_page(request):
    return render(request, 'sample-inner.html')

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')




def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account saved successfully')
            return redirect('users-registration')
        else:
            messages.error(request, 'Account creation failed')
            return redirect('users-registration')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required()
def home(request):
    return render(request, 'home.html')