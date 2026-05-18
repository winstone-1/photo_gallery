from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('photo/<int:pk>/', views.photo_detail_view, name='photo_detail'),
    path('photo/<int:pk>/like/', views.like_photo_view, name='like_photo'),
]