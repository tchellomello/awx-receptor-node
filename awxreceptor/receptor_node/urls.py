from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:param>/', views.render_config, name='render_config'),
    path('<str:param>/', views.render_config, name='render_config'),
]