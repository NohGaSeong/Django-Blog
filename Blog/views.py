import logging
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .form import MemberForm, SignupForm
from django.urls import reverse
from django.http import HttpResponseRedirect

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
            return redirect('login')
        elif form.is_valid() != 1:
            logging.warning("되지 않았어요!")
    form = SignupForm()
    return render(request, 'signup.html', {'form':form})

def main(request):
    if request.method == 'POST':
        memberName = request.POST.get('memberName')
        password = request.POST.get('password')
        member = Member.objects.get(memberName = memberName, password = password)
        if member is not None:
            request.session['memberid'] = member.id
            return render(request, 'main.html', {'memberId' : member.name})
        else :
            return redirect('login')
    return render(request, 'main.html')