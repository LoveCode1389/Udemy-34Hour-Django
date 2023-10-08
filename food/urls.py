from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    #/food/
    path('', views.index, name='index'),
    #/food/1
    path('<int:id>/', views.detail, name='detail'),
    path('item/', views.item, name='item'),
    path('contact/', views.contact, name='contact'),
]
