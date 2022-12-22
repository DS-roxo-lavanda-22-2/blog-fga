from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/<id>', views.courses, name='courses')
]