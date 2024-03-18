# Generated by Django 5.0.2 on 2024-03-03 15:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='passwoard',
            new_name='password',
        ),
        migrations.AddField(
            model_name='signup',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=120),
        ),
    ]