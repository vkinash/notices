from django.urls import path

from notice_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
