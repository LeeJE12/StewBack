# Generated by Django 5.0.7 on 2024-07-29 06:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_user_familyid_alter_family_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='familycode',
        ),
        migrations.AlterField(
            model_name='family',
            name='users',
            field=models.ManyToManyField(related_name='families', to=settings.AUTH_USER_MODEL),
        ),
    ]