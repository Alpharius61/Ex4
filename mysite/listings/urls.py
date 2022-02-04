from django.urls import path
from listings import views

app_name = 'listings'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    path('add', views.add, name='add'),
]
