# Generated by Django 3.0.2 on 2020-02-07 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('winery', models.CharField(max_length=70)),
                ('country', models.CharField(max_length=30)),
                ('province', models.CharField(max_length=35)),
                ('variety', models.CharField(max_length=40)),
                ('points', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(max_length=144, upload_to='wine_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Wine')),
            ],
        ),
    ]