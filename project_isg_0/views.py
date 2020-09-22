from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import TestForm

# Create your views here.

def home(request):
    my_dict = {
    'insert_something':"views.pyのinsert_something部分です。",
    'name':'yarita',
    'form':TestForm(),
    'insert_forms':'初期値',
    }
    if (request.method == 'POST'):
        my_dict['insert_forms'] = '文字列:' + request.POST['text'] + '<br>整数型:' + request.POST['num']
        my_dict['form'] = TestForm(request.POST)

    return render(request,'project_isg_0/home.html',my_dict)