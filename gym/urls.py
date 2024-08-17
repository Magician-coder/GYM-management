"""
URL configuration for gym project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('fee_status/', views.fee_status, name='fee_status'),
    path('daily_attendance/', views.daily_attendance, name='daily_attendance'),
    path('clear_daily_attendance/', views.clear_daily_attendance, name='clear_daily_attendance'),
    path('remove_customer/', views.remove_customer, name='remove_customer'),
    path('pay_fees_later/', views.pay_fees_later, name='pay_fees_later'),
    path('admin/', admin.site.urls),
]

