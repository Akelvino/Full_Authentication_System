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




# 
#     <form action="" method="POST">
#         {% csrf_token %}
#       <div ">
#         
#         <div>
#           <label class="text-slate-900 text-sm font-medium mb-2 block">Confirm Password</label>
#           {{ form.password2 }}
#         </div>
#       </div>
#       <div class="mt-12">
#         <button
#           type="submit"
#           class="w-full py-3 px-4 text-sm tracking-wider font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none cursor-pointer"
#         >
#           Confirm password
#         </button>
#       </div>
#     </form>
#   </div>
# </div>
# {% endblock content %} -->

