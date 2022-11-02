# Generated by Django 2.2.5 on 2022-10-31 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_cert_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_cert_image',
            field=models.ImageField(blank=True, null=True, upload_to='certificate'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(choices=[('FCC Resposive Web Design', 'FCC Resposive Web Design'), ('FCC Front End Development Libraries', 'FCC Front End Development Libraries'), ('FCC Back End Development and APIs', 'FCC Back End Development and APIs'), ('FCC Scientific Computing with Python', 'FCC Scientific Computing with Python'), ('FCC Data Analysis with Python', 'FCC Data Analysis with Python'), ('M&J Marketplace', 'M&J Marketplace')], max_length=50, null=True),
        ),
    ]
