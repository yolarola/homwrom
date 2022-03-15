from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.template.defaultfilters import safe


class Post(models.Model):
    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'

    nazvanie = models.CharField('Название поста', max_length=255,)
    user = models.ForeignKey(User,verbose_name='Пользователь',null=True, on_delete=models.CASCADE)
    data_sozdania = models.DateField('Дата создания', auto_now_add=True)
    text_posta = models.TextField('Текст поста')
    img = models.ImageField('Фото поста', null=True, blank=True)

    def get_img(self):
        if self.img:
            return safe(f'<img src = "{self.img.url}">')
        return ''

class PhotoPostov(models.Model):
    class Meta:
        verbose_name = 'Фото поста'
        verbose_name_plural = 'Фото постов'

    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.PROTECT)
    img = models.ImageField('Фото поста')

class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    category = models.ForeignKey(Category, verbose_name= 'Категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', max_length=255)
    structure = models.CharField(verbose_name='Состав', max_length=255)
    price = models.IntegerField(verbose_name='Цена',)
    weight = models.IntegerField(verbose_name='Вес',)
    color = models.CharField(verbose_name='Цвет',max_length=255)
    size = models.CharField(verbose_name='Габариты',max_length=255)
    img = models.ImageField('Изображение')

class Shelf(models.Model):
    class Meta:
        verbose_name='Полка'
        verbose_name_plural='Полки'

    number = models.CharField(verbose_name='Номер', max_length=255)
    block = models.CharField(verbose_name='Блок', max_length=255)
    row = models.IntegerField(verbose_name='Ряд', )
    place = models.CharField(verbose_name='Место',max_length=255)

class Cell(models.Model):
    class Meta:
        verbose_name='Ячейка'
        verbose_name_plural='Ячейки'

    shelf = models.ForeignKey(Shelf,verbose_name='Стелажи',on_delete=models.CASCADE)
    volume = models.IntegerField(verbose_name='Объем')
    product= models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество')


class Arrival(models.Model):
    class Meta:
        verbose_name='Приход'
        verbose_name_plural='Приходы'

    date = models.DateField(verbose_name='Дата')
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    supplier = models.CharField(verbose_name='Поставщик',max_length=255)
    quantity = models.IntegerField(verbose_name='Количество')

class Expenditure(models.Model):
    class Meta:
        verbose_name='Расход'
        verbose_name_plural='Расходы'

    date = models.DateField(verbose_name='Дата')
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    supplier = models.CharField(verbose_name='Поставщик',max_length=255)
    quantity = models.IntegerField(verbose_name='Количество')