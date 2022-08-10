from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .form import MemberForm, SignupForm

def hello(request):
    context = {
        'hello' : 'hello Django!'
    }
    return render(request, 'hello.html', context)

def login(request):
    form = MemberForm()
    return render(request, 'login.html', {'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:login')
    form = SignupForm()
    return render(request, 'signup.html', {'form':form})