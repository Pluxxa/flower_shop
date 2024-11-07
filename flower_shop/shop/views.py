from django.shortcuts import render, get_object_or_404
from .models import Flower
from django.shortcuts import redirect


def home(request):
    flowers = Flower.objects.all()
    return render(request, 'shop/home.html', {'flowers': flowers})

def register(request):
    return render(request, 'shop/register.html')  # Шаблон для страницы регистрации

# Представление для отображения каталога цветов
def flower_list(request):
    flowers = Flower.objects.all()  # Получаем все цветы из базы данных
    flowers_dict = {flower.id: flower for flower in flowers}  # Создаем словарь с ключами — ID цветов
    return render(request, 'shop/flower_list.html', {'flowers': flowers, 'flowers_dict': flowers_dict})

# Представление для отображения деталей конкретного цветка
def flower_detail(request, pk):
    flower = get_object_or_404(Flower, pk=pk)  # Получаем цветок по его первичному ключу
    return render(request, 'shop/flower_detail.html', {'flower': flower})

# Представление для добавления цветка в корзину
# Пример в представлении
def add_to_cart(request, pk):
    flower = get_object_or_404(Flower, pk=pk)
    cart = request.session.get('cart', {})
    cart[pk] = cart.get(pk, 0) + 1  # Увеличиваем количество на 1
    request.session['cart'] = cart
    return redirect('flower_list')

def contacts(request):
    return render(request, 'shop/contacts.html')  # Создайте шаблон для страницы контактов

def cart(request):
    return render(request, 'shop/cart.html')  # Создайте шаблон для страницы корзины
