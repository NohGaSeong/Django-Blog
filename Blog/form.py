from dataclasses import fields
from tkinter import Widget
from django import forms

from .models import Board, Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['memberName', 'password']
        widgets = {
            'password' : forms.PasswordInput
        }