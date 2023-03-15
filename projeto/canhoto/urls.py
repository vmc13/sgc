from django.urls import path
from projeto.canhoto import views

app_name = 'canhoto'

urlpatterns = [
    path('', views.canhoto_list, name='produto_list')
]

