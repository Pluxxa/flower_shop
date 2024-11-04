from django.db import models
from django.contrib.auth.models import User

# Модель для цветов (товаров)
from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='flowers/')

    def __str__(self):
        return self.name

# Модель для заказов
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, сделавший заказ
    flowers = models.ManyToManyField(Flower, through='OrderItem')  # Связь с цветами через промежуточную таблицу
    delivery_address = models.CharField(max_length=255)  # Адрес доставки
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания заказа
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления
    status = models.CharField(max_length=50, choices=[
        ('new', 'New'),
        ('processed', 'Processed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ], default='new')  # Статус заказа

    def __str__(self):
        return f"Order {self.id} by {self.user}"

# Промежуточная модель для связи цветов и заказов
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()  # Количество
