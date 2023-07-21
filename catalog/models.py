from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):

    name = models.CharField(max_length=150, verbose_name='Категория')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    Imag = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.category} {self.price} {self.date_of_creation}'

    class Meta:
        verbose_name = 'Цветы'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Цветы'  # Настройка для наименования набора объектов
        db_table = 'catalog'
        db_table_comment = 'КАТАЛОГ ЦВЕТОВ И РАСТЕНИЙ'
        ordering = ['name']
