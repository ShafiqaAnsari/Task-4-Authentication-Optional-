from django.contrib import admin
from django.urls import path, include
from assignment4_app import views
from .views import books_list_create, books_RUD

urlpatterns = [
    path('bookapi/',books_list_create.as_view()),
    path('bookapi/<int:pk>', books_RUD.as_view()),

]