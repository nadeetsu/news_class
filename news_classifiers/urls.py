from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news-home'),
    path('content/', views.content, name='news-content'),
    path('about/', views.about, name='news-about'),
    path('trend/', views.trend, name='news-trend'),
]