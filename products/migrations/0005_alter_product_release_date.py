# Generated by Django 3.2 on 2022-11-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20221127_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
