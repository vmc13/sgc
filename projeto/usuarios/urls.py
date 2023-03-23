from django.urls import path
from projeto.canhoto import views
from django.contrib.auth import views as auth_views

app_name = 'usuarios'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name = 'login.html'
    ), name="login"),
]

