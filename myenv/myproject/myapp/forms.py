from django import forms
from .models import book,signup


class bookForm(forms.ModelForm):
    class Meta:
        model=book
        fields="__all__"
        widget={}

class signupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields="__all__"
        widget={}