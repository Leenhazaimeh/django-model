# Generated by Django 3.2.6 on 2021-08-31 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='descreption',
            field=models.TextField(blank=True),
        ),
    ]