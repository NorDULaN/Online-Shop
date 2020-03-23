# Generated by Django 2.2 on 2020-02-05 23:37

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loginapp', '0006_auto_20200205_2227'),
        ('tradeapp', '0004_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods', django.contrib.postgres.fields.jsonb.JSONField()),
                ('date', models.DateField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('wc', 'wc'), ('wb', 'wb'), ('fb', 'fb')], default='wc', max_length=10)),
                ('supplier_status', models.CharField(choices=[('uv', 'uv'), ('v', 'v')], default='uv', max_length=10)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loginapp.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', related_query_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]