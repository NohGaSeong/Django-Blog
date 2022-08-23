import logging
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import is_valid_path
from .form import MemberForm, SignupForm, BoardWriteForm, Board, Member
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
    # board 의 모든 데이터를 부른다.
    boardList = Board.objects.all()

    if request.method == 'POST':
        memberName = request.POST.get('memberName')
        password = request.POST.get('password')
        member = member.objects.get(memberName = memberName, password = password)
        if member is not None:
            request.session['memberid'] = member.id
            return render(request, 'main.html', {'boardList' : boardList})
        else :
            return redirect('login')
    return render(request, 'main.html', {'boardList':boardList})

def write(request):
    if request.method == 'POST':
        form = BoardWriteForm(request.POST)
        if form.is_vaild():
            form.save()
            return redirect('main')
    member_id = request.session['memberId']
    member = get_object_or_404(Member, pk = member_id)
    form = BoardWriteForm(initial={'member':member})
    return render(request, 'write.html', {'form':form, 'member':member})
    