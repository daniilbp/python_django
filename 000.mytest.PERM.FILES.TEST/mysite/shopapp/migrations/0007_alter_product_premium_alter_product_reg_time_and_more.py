# Generated by Django 4.1.5 on 2023-01-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0006_alter_product_premium_alter_product_reg_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='premium',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='reg_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='small_num',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
