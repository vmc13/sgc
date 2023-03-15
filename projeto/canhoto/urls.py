from django.urls import path
from projeto.canhoto import views

app_name = 'canhoto'

urlpatterns = [
    path('', views.canhoto_list, name='canhoto_list'),
    path('<int:pk>', views.canhoto_detail, name='canhoto_detail'),
    path('add/', views.CanhotoCreate.as_view(), name='canhoto_add')
]

