# Generated by Django 3.2 on 2022-11-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]
