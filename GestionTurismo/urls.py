from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'), 
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
