# Generated by Django 3.0.2 on 2020-02-19 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200207_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='image',
        ),
    ]
