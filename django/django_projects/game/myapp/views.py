from cgitb import reset
from django.shortcuts import render
import random


def index(request):
    return render(request,"index.html")

def hadeel(request):
    # if 'number' in request.session:
    request.session['number'] = random.randint(1,100)
    if int(request.session['number']) == int(request.POST['search']):
        print('true')
        result = "true"
    elif int(request.session['number']) > int(request.POST['search']):
        print('Too high!')
        result = "too high"
    else:
        print('Too low!')
        result = "too low"
    cotext={
    "number_on_show":  result
    }
    
    return render(request,"index.html",context=context)
