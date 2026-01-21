from django.urls import path
from .views import RegisterView,UserLoginView,user_logout,dashboard

urlpatterns = [
    # path('',home_page,name='home'),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',user_logout,name='logout'),
    path('dashboard/',dashboard, name="dashboard")
]