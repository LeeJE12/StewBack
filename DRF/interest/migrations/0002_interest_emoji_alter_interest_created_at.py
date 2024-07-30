# Generated by Django 5.0.7 on 2024-07-30 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='emoji',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]