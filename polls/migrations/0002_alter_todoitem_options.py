# Generated by Django 5.1.5 on 2025-02-09 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitem',
            options={'ordering': ('id',), 'verbose_name': 'ToDo Item'},
        ),
    ]
