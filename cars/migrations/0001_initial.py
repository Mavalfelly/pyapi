# Generated by Django 5.1.4 on 2024-12-06 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_make', models.CharField(verbose_name=25)),
                ('car_model', models.CharField(verbose_name=25)),
                ('car_color', models.CharField(verbose_name=25)),
            ],
        ),
    ]
