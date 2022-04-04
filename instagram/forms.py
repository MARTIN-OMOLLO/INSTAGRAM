from .models import Details
from django import forms
from django.contrib.auth.forms import UserCreationForm
#......
class NewDetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }