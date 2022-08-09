from django.db import models

class Member(models.Model):
    memberName = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now = True)

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=256)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    createDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now = True)