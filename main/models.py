from unicodedata import category
from django.db import models
from tables import Description

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 50, null = True)
    last_name = models.CharField(max_length = 50, null = True)
    about_me = models.TextField(null = True, blank = False)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'


class Category(models.Model):
    names = [
        ('FCC Resposive Web Design', 'FCC Resposive Web Design'),
        ('FCC Front End Development Libraries', 'FCC Front End Development Libraries'),
        ('FCC Back End Development and APIs', 'FCC Back End Development and APIs'),
        ('FCC Scientific Computing with Python', 'FCC Scientific Computing with Python'),
        ('FCC Data Analysis with Python', 'FCC Data Analysis with Python'),
        ('MJ Marketplace', 'MJ Marketplace')
    ]
    user = models.OneToOneField(ondelete = models.SET_NULL, null = True, blank = True)
    category_name = models.CharField(max_length = 50, null = True)
    category_description = models.TextField(null = True, blank = False)
    category_image = models.ImageField(null = True, blank = True, upload_to='category')

    def __str__(self):
        return f'{self.category_name}'

class Project(models.Model):
    user = models.OneToOneField(User, ondelete=models.SET_NULL, null = True, blank = True)
    category = models.OneToOneField(Category, ondelete=models.SET_NULL, null = True, blank = True)
    project_name = models.CharField(max_length = 50, null = True)
    project_description = models.TextField(null = True, blank = False)
    project_image = models.ImageField(null = True, blank = True, upload_to='project')

    def __str__(self):
        return f'{self.project_name}'