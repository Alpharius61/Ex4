from django.urls import path
from bands import views as b_views

# On donne un nom à l'app
app_name = "bands"
urlpatterns = [
    path('', b_views.bands, name='index'),
    path('<int:band_id>/', b_views.band_detail, name='detail'),
    path('bandAdd', b_views.bandAdd, name='bandAdd' ),
    path('bandUp', b_views.bandUp, name='bandUp' ),
]
