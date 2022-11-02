from django.shortcuts import render
from matplotlib.collections import Collection
from .models import *
from django.views.generic import DetailView




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

class collection_details(DetailView):
    model = Category
    def get_context_data(self, *args, **kwargs):
        context = super(collection_details, self).get_context_data(*args, **kwargs)
        category = Category.objects.get(pk=self.get_object().pk)
        context['projects'] = category.project_set.all()
        return context


