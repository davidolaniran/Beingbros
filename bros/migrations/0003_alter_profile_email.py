# Generated by Django 3.2.4 on 2021-07-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bros', '0002_auto_20210701_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=150),
        ),
    ]
