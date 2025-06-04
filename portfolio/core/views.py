from django.shortcuts import render, redirect
from .models import Project, contact
# Create your views here.

def index(request):
    project= Project.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.objects.create(
            Name=name,
            Email=email,
            message=message
        )
        return redirect('index')
    queryset = contact.objects.all()
    context = {
        'queryset': queryset
        , 'projects': project
    }
        
    return render(request, 'core/home.html',context)
