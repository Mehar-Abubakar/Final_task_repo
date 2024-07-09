from django.shortcuts import render
from .models import Contact,UserProfile

def home(request):
    user_profile = UserProfile.objects.first()  # Assuming there's only one user profile
    return render(request, 'home.html', {'user_profile': user_profile})

def project(request):
    return render(request, 'project.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
    return render(request, 'home.html')
