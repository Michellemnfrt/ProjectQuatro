from . import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('repairs/list', views.repair_list, name='repair_list'),
    path('repairs/<int:pk>', views.repair_detail, name='repair_detail'),
    path('repairs/new', views.repair_create, name='repair_create'),
    # path('repairs/<int:pk>/edit', views.repair_edit, name='repair_edit'),
    path('repairs/<int:pk>/delete', views.repair_delete, name='repair_delete'),

    path('cars', views.car_list, name='car_list'),
    path('cars/<int:pk>', views.car_detail, name='car_detail'),
    path('cars/new', views.car_create, name='car_create'),
    path('cars/<int:pk>/edit', views.car_edit, name='car_edit'),
    path('cars/<int:pk>/delete', views.car_delete, name='car_delete'),

    path('favorites/<int:car_id>/create',
         views.add_favorite, name='add_favorite'),
    path('favorites/<int:car_id>/remove',
         views.remove_favorite, name='remove_favorite')
]
