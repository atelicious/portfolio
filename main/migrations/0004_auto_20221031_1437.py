# Generated by Django 2.2.5 on 2022-10-31 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_certificates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_cert_description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_cert_image',
        ),
    ]
