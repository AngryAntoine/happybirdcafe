from django import forms
from .models import YourFeeder


class YourFeederForm(forms.ModelForm):

    class Meta:
        model = YourFeeder
        fields = ('image', 'pupil_name', 'pupil_age', 'school', 'text')
