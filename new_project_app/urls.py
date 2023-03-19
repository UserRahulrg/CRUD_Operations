
from django.urls import path
from django.shortcuts import render
from new_project_app.views import *

urlpatterns=[
    path('home/',new_project_app_home),
    path('searchstudent/',search_student_data),
    path('modifystudent/',modify_student_data),
    path('showallstudent/',showall_student_data),
    path('deletestudent/',delete_student_data),
    path('addstudent/',add_student_data),
    
    
]