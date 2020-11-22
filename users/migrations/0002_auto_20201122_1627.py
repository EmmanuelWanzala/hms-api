# Generated by Django 3.1.3 on 2020-11-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profile_pic',
            field=models.CharField(blank=True, default='https://www.iconfinder.com/data/icons/user-pictures/100/unknown-512.png', max_length=255, null=True),
        ),
    ]