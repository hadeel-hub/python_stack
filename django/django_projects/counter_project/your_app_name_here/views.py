from django.shortcuts import render,redirect, HttpResponse

def counter(request):
   if 'count' in request.session:
      request.session ['count']+=1
   else:
    request.session['count']=0
    return render( request,"index.html")

def destroy(request):
    del request.session['count']
    return redirect('/')


