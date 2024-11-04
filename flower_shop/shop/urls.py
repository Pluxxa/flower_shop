from django.urls import path
from . import views
from .views import home
from .views import flower_list, contacts, cart
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('flower/<int:pk>/', views.flower_detail, name='flower_detail'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('flowers/', flower_list, name='flower_list'),  # Страница с цветами
    path('contacts/', contacts, name='contacts'),  # Страница контактов
    path('cart/', cart, name='cart'),  # Страница корзины
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

