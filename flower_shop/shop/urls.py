from django.urls import path
from . import views
from .views import home
from .views import flower_list, contacts, cart
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),              # Главная страница
    path('flower/<int:pk>/', views.flower_detail, name='flower_detail'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('flowers/', views.flower_list, name='flower_list'),  # Каталог
    path('contacts/', views.contacts, name='contacts'),       # Контакты
    path('cart/', views.cart, name='cart'),                   # Корзина
    path('register/', views.register, name='register'),       # Регистрация
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('account/', views.account, name='account'),  # Личный кабинет
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

