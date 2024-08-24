from django.urls import path
from . import views

urlpatterns = [
    path('dados/', views.lista_dados, name='lista_dados')
]