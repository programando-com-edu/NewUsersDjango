from django.urls import path
from app_cad_usuarios import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('view/<int:pk>/', views.view, name='view'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),

]
