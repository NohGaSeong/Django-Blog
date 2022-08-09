from django.shortcuts import render


def hello(request):
    context = {
        'hello' : 'hello Django!'
    }
    return render(request, 'hello.html', context)