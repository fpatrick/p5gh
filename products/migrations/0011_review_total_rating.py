# Generated by Django 3.2 on 2022-11-27 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='total_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
