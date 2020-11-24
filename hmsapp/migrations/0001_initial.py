# Generated by Django 3.1.3 on 2020-11-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_title', models.CharField(max_length=150)),
                ('app_details', models.TextField()),
                ('app_status', models.IntegerField(default=0)),
                ('app_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_fee', models.PositiveIntegerField(default=0)),
                ('service_fee', models.PositiveIntegerField(default=0)),
                ('medication_fee', models.PositiveIntegerField(default=0)),
                ('doc_fee', models.PositiveIntegerField()),
                ('total_amount', models.PositiveIntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('bill_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_title', models.CharField(max_length=150)),
                ('diagnosis', models.TextField()),
                ('medication_quantity', models.PositiveIntegerField(default=0)),
                ('admission_days', models.PositiveIntegerField(default=0)),
                ('case_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=100)),
                ('med_cost_price', models.PositiveIntegerField()),
                ('med_manufacture', models.CharField(max_length=100)),
                ('med_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('service_cost', models.PositiveIntegerField()),
                ('service_description', models.TextField()),
            ],
        ),
    ]
