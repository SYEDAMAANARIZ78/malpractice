from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import Malpracticentry
from .models import Malpracticentry,Login

class MalpracticentryForm(forms.ModelForm):
    class Meta:
        model = Malpracticentry
        fields = "__all__"

class LoginnForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"
        