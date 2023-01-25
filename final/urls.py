"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from second import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('',views.blank, name='blank'),
     path('incoming_data/',views.incoming_data, name='incoming_data'),
     path('users/',views.disp_data, name='disp_data'),
     path('table/',views.table, name='table'),
     path('signup/',views.Signup, name='signup'),
     path('login/',views.user_login, name='login'),
     path('logout/',views.user_logout, name='logout'),
     path('disp_table/',views.disp_table, name='disp_table'),
     path('admin_profile/',views.admin_profile, name='admin_profile'),
     path('front_admin/<int:id>',views.front_admin, name='front_admin'),
    #  path('profile/',views.profile, name='profile'),
    #  path('adminprofile/',views.admin_profile, name='admin_profile'),
    #  path('userdisp/<int:id>',views.userdisp, name='userdisp'),
    
    
]

