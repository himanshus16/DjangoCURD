from django.urls import path
from . import views

urlpatterns = [
    path('', views.f1,name="home" ),
    path('insert/', views.f2,name="insert"),
    path('display/', views.f3, name="display"),
    path('update/<int:pk>', views.f4, name="update"),
    path('delete/<int:n>/', views.f5, name="delete"),
]