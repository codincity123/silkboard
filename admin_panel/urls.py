from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin_login',admin_login_request,name="admin_login"),
    path('admin_logout',admin_logout_request,name="admin_logout"),

    path("mod1",admin_home,name="admin_home"),
    path("regist",register,name="regist"),
    path("export",export_users_xls,name="export"),
    path("",users,name="users"),
    path("update/<str:id>/",updatedata,name='update'),
    # mod2
    path("mod2",adminMod2,name="mod2"),
    path("export2",export_users_xls2,name="export2"),

    #  # mod3
    path("mod3",adminMod3,name="mod3"),
    path("export3",export_users_xls3,name="export3"),

    # #mod4
    path("mod4",adminMod4,name="mod4"),
    path("export4",export_users_xls4,name="export4"),

    

    path("delete/<str:username>/",del_user,name="delete"),
    # # delete
    path("mod1delete/<str:username>/",mod1delete,name="mod1delete"),
    path("mod2delete/<str:username>/",mod2delete,name="mod2delete"),
    path("mod3delete/<str:username>/",mod3delete,name="mod3delete"),
    path("mod4delete/<int:id>/",mod4delete,name="mod4delete"),

]
