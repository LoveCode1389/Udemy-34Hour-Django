from django.urls import path
from . import views

urlpatterns = [
    #/food/
    path('', views.index, name='index'),
    #/food/1
    path('<int:id>/', views.detail, name='detail'),
    path('item/', views.item, name='item'),
]
