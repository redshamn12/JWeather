from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

handler404 = 'sweather.views.page_not_found'