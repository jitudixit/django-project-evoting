from django.contrib import admin
from django.urls import path
from evotingapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.uhome),
    path('uhome/', views.uhome),
    path('ureg/', views.ureg),
    path('uvreg/',views.uvreg),
    path('userv/',views.userv),
    path('ucontact/',views.ucontact),
    path('uabout/',views.uabout),
    path('vot/',views.vot),
    path('voted/',views.voted),
    path('candireg/',views.candireg),
    path('contactaction/',views.contactaction),
    path('adminhome/',views.adminhome),
    path('adminlogin/',views.adminlogin),
    path('partylogin/',views.partylogin),
    path('partyhome/',views.partylogin),
    path('partynews/',views.partynews),
    path('uregaction/',views.uregaction),
    path('uregactionone/',views.uregactionone),
    path('usersaction/',views.usersaction),
    path('adminloginaction/',views.adminloginaction),
    path('partyloginaction/',views.partyloginaction),
    path('uvregaction/',views.uvregaction),
]
