from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('file_alt/', views.index_alt, name='index_alt'),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('my_form/',views.my_form, name='my_form'),
    #path('search/<int:data_id>/', views.search, name='search/<int:data_id>'),
    path('search/', views.search, name='search'),
    path('detailview/<int:d_id>/', views.detailview, name='detailview'),
]