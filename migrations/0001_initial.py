# Generated by Django 4.2.5 on 2023-10-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=100)),
                ('massage', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'ContactForm',
            },
        ),
    ]
