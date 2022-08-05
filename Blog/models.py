from curses import ACS_GEQUAL
from tkinter.simpledialog import askinteger
from venv import create
from django.db import models
from django.forms import DateTimeField

class Member(models.Model):
    memberName = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    name = models.CharField(max_length=12)
    age = models.CharField(max_length=3)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    createDate = DateTimeField(auto_now_add = True)
    updateDate = DateTimeField(auto_now = True)