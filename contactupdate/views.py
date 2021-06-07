from django.shortcuts import render
from .models import Users
from django.http import HttpResponse
# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['text']
        print(name, phone, email, message)
        obj = Users()
        obj.name = name
        obj.phone = phone
        obj.email = email
        obj.message = message
        obj.save()
    return render(request, 'contact.html')
