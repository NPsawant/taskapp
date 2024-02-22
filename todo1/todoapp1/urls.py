from django.urls import path
from todoapp1 import views

urlpatterns = [
    path('contact',views.contact_page),
    path('about',views.about_page),
    path('products',views.products_page),
    path('awards',views.awards_page),
    path('home',views.home_page),
    path('add_task',views.add_task),
    path('dtl',views.dtl), #dJANGO TEMPLATE LANG TO CHECK THE CONCEPT OF CONTEXT
    path('delete/<rid>',views.delete_task),#/<rid> is added bcz we pass the http://127.0.0.1:8000/delete/1
    path('edit/<rid>',views.edit_task),
    path('completed/<rid>',views.mark_completed),


] 


