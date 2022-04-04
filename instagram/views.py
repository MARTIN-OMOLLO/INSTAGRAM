from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import  Signup

# Create your views here.

#.....
def home(request):
    return render(request,'instagram/index.html')
# @login_required(login_url='/accounts/login/')
# def new_details(request,details_id):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewDetailsForm(request.POST, request.FILES)
#         if form.is_valid():
#             detail = form.save(commit=False)
#             detail.editor = current_user
#             detail.save()
#         return redirect('NewsToday')

#     else:
#         form = NewDetailsForm()
#     return render(request, 'new_details.html', {"form": form})

def register(request):
    form = Signup()
    userid = request.user.id
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    
    return render(request, 'registration/register.html', {"form":form, "userid":userid})

