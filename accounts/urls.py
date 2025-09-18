from . import views
from django.urls import path

urlpatterns = [
    path('accounts/', views.users_list, name='user-list'),
]