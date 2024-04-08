from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('allstudents/', views.allstudents, name='allstudents'),
    path('attendance/', views.attendance, name='attendance'),
    path('students/attendance/', views.allattendance, name='allattendance'),
]