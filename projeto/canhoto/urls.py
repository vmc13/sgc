from django.urls import path
from projeto.canhoto import views

app_name = 'canhoto'

urlpatterns = [
    path('', views.canhoto_list, name='canhoto_list'), #CanhotoList.as_vie() -> to pagination
    path('<int:pk>', views.canhoto_detail, name='canhoto_detail'),
    path('add/', views.CanhotoCreate.as_view(), name='canhoto_add'),
    path('<int:pk>/edit/', views.CanhotoUpdate.as_view(), name='canhoto_edit'),
    path('import/csv/', views.import_csv, name='import_csv'),
]

