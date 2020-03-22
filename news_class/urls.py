from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('news_classifiers.urls')),
    path('admin/', admin.site.urls),
]
