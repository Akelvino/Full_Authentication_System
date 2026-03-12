from django.shortcuts import render
from .forms import UserRegistration

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def RegisterView(request):
    if (request.method == 'POST'):
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegistration()
    return render(request, 'core/register.html', {'form':form})

def LoginView(request):
    return render(request, 'core/login.html')