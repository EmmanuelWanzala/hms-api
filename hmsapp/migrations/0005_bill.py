# Generated by Django 3.1.3 on 2020-11-12 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0004_case'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_fee', models.PositiveIntegerField(default=0)),
                ('medication_fee', models.PositiveIntegerField(default=0)),
                ('doc_fee', models.PositiveIntegerField()),
                ('total_amount', models.PositiveIntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('bill_date', models.DateTimeField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hmsapp.case')),
            ],
        ),
    ]