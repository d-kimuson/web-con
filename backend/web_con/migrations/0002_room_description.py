# Generated by Django 3.1.2 on 2020-11-03 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_con', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
