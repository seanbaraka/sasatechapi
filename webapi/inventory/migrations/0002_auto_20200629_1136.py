# Generated by Django 3.0.7 on 2020-06-29 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product description',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
