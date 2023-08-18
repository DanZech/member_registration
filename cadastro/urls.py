# from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    # rota, view responsável, nome de referencia
    path('', views.home, name='home'),
    path('users/', views.users, name='users_list'),
    #path('admin/', admin.site.urls),
]
