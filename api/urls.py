from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    path('games/', views.GamesView.as_view(), name='all-games'),
    path('todos/', views.TodosView.as_view(), name='all-todos'),
    path('todos/<int:todos_id>', views.TodosView.as_view(), name='all-todos'),
]
