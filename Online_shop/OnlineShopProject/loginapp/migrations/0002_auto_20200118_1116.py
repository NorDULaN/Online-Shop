# Generated by Django 2.2 on 2020-01-18 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiletable',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
