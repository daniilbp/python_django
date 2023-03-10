# Generated by Django 4.1.5 on 2023-01-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='premium',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='reg_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='small_num',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]
