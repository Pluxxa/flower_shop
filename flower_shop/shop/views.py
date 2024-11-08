from django.shortcuts import render, get_object_or_404, redirect
from .models import Flower
from django.contrib.auth.models import User  # Если используем встроенную модель User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    flowers = Flower.objects.all()
    return render(request, 'shop/home.html', {'flowers': flowers})


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


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Проверка, существует ли уже такой пользователь
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует')
            return redirect('register')

        # Создание нового пользователя
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # Автоматическая авторизация после регистрации
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('home')  # Замените на нужный URL после регистрации

    return render(request, 'shop/register.html')


@login_required
def account(request):
    return render(request, 'shop/account.html')
