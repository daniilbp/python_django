# Generated by Django 4.0.6 on 2023-01-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_employment', '0002_alter_vacancy_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('description', models.TextField(default='', verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'резюме',
                'verbose_name_plural': 'резюме',
                'permissions': {('can_publish', 'Может публиковать')},
            },
        ),
    ]
