from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),  
    path('new/', views.new, name='new'),  
    path('<int:pk>/', views.detail, name='detail'),  
    path('<int:pk>/delete/', views.delete, name='delete'), 
    path('<int:pk>/edit/', views.edit, name='edit'),  
    path('<int:item_id>/place_order/', views.purchase_item, name='place_order'),   
    path('<int:item_id>/shipping_details/', views.shipping_details, name='shipping_details'),  
    path('order/confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'), 
    path('<int:pk>/place_order/', views.purchase_item, name='place_order')
]
