
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name="home"),
    # path('registration/',registration.as_view(),name="regist"),
    # path("register/",register, name="register"),
    path("logout",logout_request, name="logout"),
    path("login", login_request, name="login"),
    path("mod1/",mod1.as_view(),name="mod11"),
    path("mod2",mod2.as_view(),name="mod22"),
    path("mod3",mod3.as_view(),name="mod33"),
    path("mod4",mod4.as_view(),name="mod44"),

    path("moddata1",moddata1,name="moddata1"),
    path("moddata2",moddata2,name="moddata2"),
    path("moddata3",moddata3,name="moddata3"),
    path("moddata4",moddata4,name="moddata4"),

    path("update1/<str:id>/",updatemod1,name="update1"),
    path("update2/<str:id>/",updatemod2,name="update2"),
    path("update3/<str:id>/",updatemod3,name="update3"),
    path("update4/<int:id>/",updatemod4,name="update4"),
    # path("update5/<str:id>/",updatemod5,name="update5"),
    # path("update6/<str:id>/",updatemod6,name="update6"),
]
