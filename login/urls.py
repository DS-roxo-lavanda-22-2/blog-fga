from django.urls import path

from . import views
from.views import login

urlpatterns = [
    path('login/', views.login, name='login'),
]