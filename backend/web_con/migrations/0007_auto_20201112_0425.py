# Generated by Django 3.1.3 on 2020-11-11 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_con', '0006_auto_20201112_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomuser',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomuser', to='web_con.room'),
        ),
    ]
