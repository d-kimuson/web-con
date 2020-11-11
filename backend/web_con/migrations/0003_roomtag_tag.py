# Generated by Django 3.1.2 on 2020-11-03 03:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web_con', '0002_room_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=127, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomTag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_con.room')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_con.tag')),
            ],
        ),
    ]
