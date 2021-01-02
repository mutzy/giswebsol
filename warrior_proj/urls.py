"""warrior_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from warriorapp import views

urlpatterns = [
    path('', views.index),
    path('file_alt/', views.index_alt),
    path('accounts/', include('django.contrib.auth.urls')),
    path('my_form/', views.my_form),
    #path('search/<int:data_id>/', views.search),
    path('search/', views.search),
    path('detailview/<int:d_id>/', views.detailview),
    path('admin/', admin.site.urls),
]
