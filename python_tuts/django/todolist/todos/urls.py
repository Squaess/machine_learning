from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [    
    path('', views.index, name='index'),    
    path('details/<int:todo_id>/', views.details, name='details'),    
    #ex: /todos/add/
    path('add/', views.add, name='add')
]