from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def education(request):
    return render(request,'education.html') 
def experience(request):
    return render(request,'experience.html')    
def projects(request):
    return render(request,'projects.html')
def certifications(request):
    return render(request,'certifications.html')           