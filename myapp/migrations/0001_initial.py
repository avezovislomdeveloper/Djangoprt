# Generated by Django 5.0.4 on 2024-05-13 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('main_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SecondImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('firt_image', models.ImageField(upload_to='')),
                ('second_image', models.ImageField(upload_to='')),
                ('third_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('about_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
