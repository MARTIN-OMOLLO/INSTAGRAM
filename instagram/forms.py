from .models import Details
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#......
# class NewDetailsForm(forms.ModelForm):
#     class Meta:
#         model = Details
#         exclude = ['editor', 'pub_date']
#         widgets = {
#             'tags': forms.CheckboxSelectMultiple(),
#         }
class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']