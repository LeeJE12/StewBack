# Generated by Django 5.0.7 on 2024-08-01 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekhashtag',
            name='weekOfMonth',
            field=models.TextField(null=True),
        ),
    ]