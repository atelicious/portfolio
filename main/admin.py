from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Certificate)