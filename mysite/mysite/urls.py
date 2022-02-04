from django.contrib import admin
from django.urls import path, include
from main import views as m_views

# Tout les urls
urlpatterns = [
    path('admin/', admin.site.urls),
    # On donne des petits noms au urls pour plus facilement les retrouver
    path('', m_views.index, name='index'),
    path('a-propos/', m_views.about, name='about'),
    path('about2/', m_views.about2),
    # Dès qu'un url commence par /bands/ est détecté,
    # il va chercher dans le fichier urls.py dans l'app bands un url qui correspond à l'actuel
    path('bands/', include('bands.urls')),
    path('listings/', include('listings.urls')),
]
