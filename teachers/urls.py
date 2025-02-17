from django.urls import path
from . import views

app_name = 'teachers'
urlpatterns = [
    path('list/', views.teacher_list, name='list'),
    path('detail/<slug:slug>/', views.teacher_detail, name='detail'),
    path('create/', views.teacher_create, name='create'),
    path('update/<int:pk>/', views.teacher_update, name='update'),
    path('delete/<int:pk>/', views.teacher_delete, name='delete'),
]
