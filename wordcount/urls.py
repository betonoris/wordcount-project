
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
]
