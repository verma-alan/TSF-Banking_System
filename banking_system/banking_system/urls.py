"""banking_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from customer import views as customer_views
from transaction import views as transaction_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',customer_views.welcome),
    path('home/',customer_views.welcome,name = 'home'),
    path('customer/',include('customer.urls')),
    path('transaction/',transaction_views.TransactionListView.as_view(),name = 'transaction-home')
]
