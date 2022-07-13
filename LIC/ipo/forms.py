from django import forms
from .models import ipo_models
from django.contrib.auth.models import User
class ipoform(forms.ModelForm):
    class Meta:
        model = ipo_models
        fields = "__all__"

class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']