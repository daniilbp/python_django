# Generated by Django 4.0.6 on 2023-01-31 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'permissions': {('can_verify', 'Может проверить')}, 'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
    ]
