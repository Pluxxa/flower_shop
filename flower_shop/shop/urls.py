from django.urls import path
from . import views
from .views import home
from .views import flower_list, contacts, cart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),              # Главная страница
    path('flower/<int:pk>/', views.flower_detail, name='flower_detail'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('flowers/', views.flower_list, name='flower_list'),  # Каталог
    path('contacts/', views.contacts, name='contacts'),       # Контакты
    path('cart/', views.cart, name='cart'),                   # Корзина
    path('register/', views.register, name='register'),       # Регистрация
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

