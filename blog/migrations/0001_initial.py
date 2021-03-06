# Generated by Django 4.0.2 on 2022-02-12 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_sozdania', models.DateField(auto_created=True, verbose_name='Дата создания')),
                ('nazvanie', models.CharField(max_length=255, verbose_name='Название поста')),
                ('avtor', models.CharField(blank=True, max_length=255, null=True, verbose_name='Автор')),
                ('text_posta', models.TextField(verbose_name='Текст поста')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото поста')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
