# Generated by Django 5.0.2 on 2024-03-03 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileapi', '0002_rename_passwoard_signup_password_signup_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='username',
            field=models.CharField(default='default_username', max_length=120),
        ),
    ]