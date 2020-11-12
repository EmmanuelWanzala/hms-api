# Generated by Django 3.1.3 on 2020-11-12 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hmsapp', '0003_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_title', models.CharField(max_length=150)),
                ('diagnosis', models.TextField()),
                ('admission', models.BooleanField(default=False)),
                ('case_date', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_doctor', to=settings.AUTH_USER_MODEL)),
                ('medication', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hmsapp.medication')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_patient', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hmsapp.service')),
            ],
        ),
    ]
