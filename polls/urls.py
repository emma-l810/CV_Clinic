from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name="registration"),
    path('registration/', views.registration, name="registration"),
    path('login', LoginView.as_view(template_name='polls/login.html'), name="login"),
    path('login/', views.login, name="login"),
    path('profile', views.profile, name="profile"),
    path('profile/', views.profile, name="profile"),
]
