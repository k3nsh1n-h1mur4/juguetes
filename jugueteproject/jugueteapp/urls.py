from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login_user, name='login_user'),
    path('auth/logout/', views.logout, name='logout'),
    path('worker/registerW/', views.registerW, name='registerW'),
    path('worker/list/', views.list, name='list'),
    path('worker/delete/<int:id>', views.deleteW, name='deleteW'),
    path('childs/registerC/<int:id>/', views.registerC, name='registerC'),
    path('childs/list/', views.listC, name='listC'),
    path('childs/delete/<int:id>', views.deleteC, name='deleteC'),
    path('valepdf/<int:id>', views.valePdf, name='valePdf'),
    path('qrcode1/<int:id>/', views.createQR, name='createQR'),
    path('qrcode/<int:id>/', views.getQrcode, name='getQrcode'),
    path('createpdf/<int:id>/', views.createpdf, name='createpdf'), 
    #path('worker/list/', views.list, name='list),
]
