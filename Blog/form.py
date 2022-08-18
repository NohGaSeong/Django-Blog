from doctest import master
from tkinter import Widget
from .models import Member,Board
from django import forms

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['memberName','password']
        widgets = {
            'password' : forms.PasswordInput
        }

class SignupForm(forms.ModelForm):
    password_check = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={'class'  : 'pw2'}))

    class Meta:
        model = Member
        fields = ['memberName','password','password_check', 'name']
        widgets = {
            'memberName': forms.TextInput(attrs={'class':'memberName'}),
            'password' : forms.PasswordInput(attrs={'class':'pw1'}),
        }

class BoardWriteForm(forms.ModelForm):
    class Meta:
        model = Board
        fileds = ['title','content','member']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'title'}),
            'content' : forms.TextInput(attrs={'class':'content'}),
            'member': forms.HiddenInput
        }