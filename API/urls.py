from django.urls import path
from . import views

app_name="API"


urlpatterns=[

    path('add_student',views.add_student),

    path('list',views.list_student),

    path('delete/<int:sid>',views.delete_student),

    path('update/<int:sid>',views.update_student),

    path('index',views.index, name='index'),

    path('home',views.home, name='home')







]
