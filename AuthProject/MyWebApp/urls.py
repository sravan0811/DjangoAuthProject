from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('help/',views.help,name='help'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register_user,name='register'),
    path('login/',auth_view.LoginView.as_view(template_name='MyWebApp/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='MyWebApp/logout.html'),name='logout'),
    path('profile/',views.profile,name='profile')
]