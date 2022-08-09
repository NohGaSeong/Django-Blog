from .models import Member,Board
from django import forms

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['memberName','password']
        widgets = {
            'password' : forms.PasswordInput
        }