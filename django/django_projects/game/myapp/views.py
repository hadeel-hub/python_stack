from django.shortcuts import render
import random


def index(request):
    return render(request,"index.html")

def hadeel(request):
    # if 'number' in request.session:
    request.session['number'] = random.randint(1,100)
    if int(request.session['number']) == int(request.POST['search']):
        print('this is number')
    elif int(request.session['number']) > int(request.POST['search']):
        print('Too high!')
    else:
        print('Too low!')
    
    return render(request,"index.html")
