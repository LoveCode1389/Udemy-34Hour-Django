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
    # add foods
    path('add', views.create_food, name='create_food'),
    # edit
    path('update/<int:id>/',views.update_food,name="update_food"),
    # delete
    path('delete/<int:id>/', views.delete_food, name='delete_food'),
]
