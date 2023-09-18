from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
path('logout/', views.index, name='index'),
path('home2/', views.index2, name='index2'),


  path('login/', views.Login, name='loginForm'),
  path('register/', views.register, name='registerForm'),
  path('edit_page_view/', views.edit_page_view, name='edit_page_view'),
  path('delete/', views.delete_student, name='delete'),

    path('addStudent/', views.addStudent, name='addStudent'),

  path('update_status/', views.update_status, name='update_status'),

  path('search/', views.search_page, name='search-students'),
  path('search/result/', views.search_student, name='search-result'),
  path('assign/', views.assign_department, name='assign-department'),

  path('assign/student/', views.search_student_id, name='search-student-id'),

  path('assign/update/', views.assign_to_student, name='assign-to-student'),

    path('ActiveStudents/', views.active, name='ActiveStudents'),
path('update_status/', views.update_status, name='update_status'),
    path('logout/', views.logout, name='logout'),
  path('signin/', views.signin, name='signin'),
  path('forget/', views.forget_password, name='forget'),
  path('newPassword/', views.newPassword, name='newPassword'),
  path('home2/', views.home_page2, name='home2'),


]