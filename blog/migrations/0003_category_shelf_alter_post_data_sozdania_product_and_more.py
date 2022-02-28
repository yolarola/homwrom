# Generated by Django 4.0.2 on 2022-02-28 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_photopostov'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255, verbose_name='Номер')),
                ('block', models.CharField(max_length=255, verbose_name='Блок')),
                ('row', models.IntegerField(verbose_name='Ряд')),
                ('place', models.CharField(max_length=255, verbose_name='Место')),
            ],
            options={
                'verbose_name': 'Полка',
                'verbose_name_plural': 'Полки',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='data_sozdania',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('structure', models.CharField(max_length=255, verbose_name='Состав')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('weight', models.IntegerField(verbose_name='Вес')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет')),
                ('size', models.CharField(max_length=255, verbose_name='Габариты')),
                ('img', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('supplier', models.CharField(max_length=255, verbose_name='Поставщик')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Расход',
                'verbose_name_plural': 'Расходы',
            },
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField(verbose_name='Объем')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.product', verbose_name='Продукт')),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.shelf', verbose_name='Стелажи')),
            ],
            options={
                'verbose_name': 'Ячейка',
                'verbose_name_plural': 'Ячейки',
            },
        ),
        migrations.CreateModel(
            name='Arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('supplier', models.CharField(max_length=255, verbose_name='Поставщик')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Приход',
                'verbose_name_plural': 'Приходы',
            },
        ),
    ]
