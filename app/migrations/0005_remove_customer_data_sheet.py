# Generated by Django 3.0.3 on 2020-05-21 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200520_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='data_sheet',
        ),
    ]
