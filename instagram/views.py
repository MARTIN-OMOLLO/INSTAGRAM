from django.shortcuts import render
from django.contrib.auth.decorators import login_required.
from .forms import NewDetailForm

# Create your views here.

#.....
@login_required(login_url='/accounts/login/')
def new_details(request,details_id):
    current_user = request.user
    if request.method == 'POST':
        form = NewDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.editor = current_user
            detail.save()
        return redirect('NewsToday')

    else:
        form = NewDetailsForm()
    return render(request, 'new_details.html', {"form": form})
