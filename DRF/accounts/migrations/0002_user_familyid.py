# Generated by Django 5.0.7 on 2024-07-28 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='familyid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]