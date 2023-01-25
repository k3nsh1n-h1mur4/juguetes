from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login_user, name='login_user'),
    path('auth/logout/', views.logout, name='logout'),
    path('worker/registerW/', views.registerW, name='registerW'),
    path('worker/list/', views.list, name='lists'),
    #path('worker/list/', views.list, name='list),
]
