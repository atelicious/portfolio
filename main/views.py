from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    user = User.objects.get(first_name='Elhy')
    categories = Category.objects.all()
    certificates = Certificate.objects.all()

    context = {
        'title': 'Welcome',
        'user' :user,
        'categories': categories,
        'certificates': certificates
    }

    return render(request, 'main/home.html', context)

