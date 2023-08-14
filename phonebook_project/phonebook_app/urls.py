from django.urls import path
from . import views

urlpatterns = [
    path('', views.phonebook_list, name='phonebook_list'),
    path('add/', views.add_entry, name='add_entry'),
    path('search/', views.search_entry, name='search_entry'),
    path('delete/', views.delete_entry, name='delete_entry'),
    path('goadd/',views.goadd,name='goadd'),
    path('gosearch/',views.gosearch,name='gosearch'),
    path('godelete/delete.html',views.godelete,name='godelete'),
    path('phonebook_list/',views.phonebook_list,name='phonebook_list')
]
