from .models import Details
#......
class NewDetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }