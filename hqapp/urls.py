from django.urls import path,include
from hqapp import views
urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('menu/',views.menu,name='menu'),
    path('introduce/',views.introduce,name='introduce'),
    path('main/',views.main,name='main'),
    path('registerlogic/',views.registerlogic,name='registerlogic'),
    path('checkrname/',views.checkrname,name='checkrname'),
    path('checkrphone/',views.checkrphone,name='checkrphone'),
    path('checkremail/',views.checkremail,name='checkremail'),
    path('checkrpwd/',views.checkrpwd,name='checkrpwd'),
    path('checklname/',views.checklname,name='checklname'),
    path('checklpwd/',views.checklpwd,name='checklpwd'),
    path('check/',views.check,name='check'),
    path('loginlogic/',views.loginlogic,name='loginlogic'),
  ]