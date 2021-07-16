from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_item.as_view(), name='add'),
    path('<str:item_definition>', views.delete, name='delete'),
    
]