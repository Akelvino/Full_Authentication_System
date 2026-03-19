from django.shortcuts import render,redirect
from .forms import UserRegistration
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def RegisterView(request):
    if (request.method == 'POST'):
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserRegistration()
    return render(request, 'core/register.html', {'form':form})

@login_required
def welcome_page(request):
    return render(request, 'core/welcomePage.html')

