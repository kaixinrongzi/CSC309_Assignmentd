from django.urls import path
from . import views

app_name='text'
urlpatterns = [
    path('data', views.data, name='data'),
    path('like', views.like, name='like'),
]