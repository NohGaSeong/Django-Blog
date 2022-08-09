from django.shortcuts import render
from .form import MemberForm

def hello(request):
    context = {
        'hello' : 'hello Django!'
    }
    return render(request, 'hello.html', context)

def login(request):
    form = MemberForm()
    return render(request, 'login.html', {'form':form})