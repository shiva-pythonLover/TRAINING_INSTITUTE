"""TRAINING_INSTITUTE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app_ADVANCED_LEARNING_INSTITUTE import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage, name="home"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('adminlogin/',views.AdminLogin.as_view(),name="adminlogin"),
    path('add_course/',views.AddCourse.as_view(),name="add_course"),
    path('view_all_courses/',views.view_all_courses,name="view_all_courses"),
    path('update/',views.Update.as_view(),name="update"),
    path('show_all_courses/', views.show_all_courses, name="show_all_courses"),
    path('feedback/',views.FeedBack.as_view(),name="feedback"),
    path('view_all_students',views.view_all_students,name="view_all_students"),



]
