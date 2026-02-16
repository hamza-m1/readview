from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='home'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
]
