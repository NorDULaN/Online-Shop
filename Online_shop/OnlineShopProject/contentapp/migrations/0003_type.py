# Generated by Django 2.2 on 2020-01-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentapp', '0002_laptop_refrigerator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=256)),
            ],
        ),
    ]
