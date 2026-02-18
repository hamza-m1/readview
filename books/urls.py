from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='home'),
    path('request_book/', views.request_book, name='request_book'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
]
