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
from softTech import views
from django.contrib import admin
from django.urls import path
from TRAINING_INSTITUTE.settings import DEBUG,STATIC_ROOT,STATIC_URL,MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('send_quote/',views.sendQuote,name="send_quote"),
    path('aboutus/',views.aboutus,name = "aboutus"),
    path('service/',views.service,name="service"),
    path('service-details/',views.serviceDetails,name="service-details"),
    path('blog/',views.blog,name="blog"),
    path('pricing/',views.pricing,name="pricing"),
    path('testimonials/',views.testimonials,name="testimonials"),
    path('team/',views.team,name="team"),
    path('terms-conditions/',views.terms_conditions,name="terms-conditions"),
    path('privacy-policy/',views.privacy_policy,name="privacy-policy"),
    path('sign-up/',views.sign_up,name="sign-up"),
    path('log-in/',views.log_in,name="log-in"),
    path('coming-soon/',views.coming_soon,name="coming-soon"),
    path('faq/',views.faq,name="faq"),
    path('blog-grid/',views.blog_grid,name="blog-grid"),
    path('blog-single/',views.blog_single,name="blog-single"),
    path('uploadvideo/',views.uploadvideo,name="uploadvideo"),
    path('online-courses/',views.online_courses,name="online-courses"),
    #path('404/',views.404,name="404"),
    #path('index-2/',views.index_2,name = "index-2")
    # path('adminlogin/',views.AdminLogin.as_view(),name="adminlogin"),
    # path('add_course/',views.AddCourse.as_view(),name="add_course"),
    # path('view_all_courses/',views.view_all_courses,name="view_all_courses"),
    # path('update/',views.Update.as_view(),name="update"),
    # path('show_all_courses/', views.show_all_courses, name="show_all_courses"),
    # path('feedback/',views.FeedBack.as_view(),name="feedback"),
    # path('view_all_students',views.view_all_students,name="view_all_students"),

]
if settings.DEBUG:
     urlpatterns = urlpatterns+static(settings.STATIC_URL, document_root = STATIC_ROOT)
     urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root = MEDIA_ROOT)

