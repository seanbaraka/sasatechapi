# Generated by Django 3.0.7 on 2020-06-28 18:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product description', models.TextField()),
                ('remarks', models.TextField(null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('buying_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vendor', models.CharField(max_length=100, null=True)),
                ('added_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='added at')),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='inventory.ServiceCategory')),
            ],
        ),
    ]
