# Generated by Django 4.1 on 2023-10-03 16:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default=None, max_length=21, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=21, null=True, validators=[django.core.validators.MaxLengthValidator(21)]),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=21, null=True, validators=[django.core.validators.MaxLengthValidator(21)]),
        ),
        migrations.AddField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=21, null=True, validators=[django.core.validators.MaxLengthValidator(21)]),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(0, 'visitor'), (1, 'admin')], default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
