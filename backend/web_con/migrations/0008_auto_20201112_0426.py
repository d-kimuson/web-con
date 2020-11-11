# Generated by Django 3.1.3 on 2020-11-11 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_con', '0007_auto_20201112_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_created', to='accounts.user'),
        ),
    ]
