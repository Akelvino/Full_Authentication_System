from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def RegisterView(request):
    return render(request, 'core/register.html')

def LoginView(request):
    return render(request, 'core/login.html')