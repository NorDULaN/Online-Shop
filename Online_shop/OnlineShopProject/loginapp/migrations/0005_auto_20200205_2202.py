# Generated by Django 2.2 on 2020-02-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_auto_20200205_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zip_number',
            field=models.CharField(max_length=256),
        ),
    ]
