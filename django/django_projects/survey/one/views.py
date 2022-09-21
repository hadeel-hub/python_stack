from django.shortcuts import render

def index(request):
    return render(request,"index.html")


def locate(request):
    name_form =request.POST['name']
    location_form=request.POST['location']
    language_form=request.POST['language']
    comment_form=request.POST['comment']
    context={
        'name1':name_form,
        'location1':location_form,
        'language1':language_form,
        'comment1':comment_form,
    }
    return render(request,"index2.html",context=context)
    


