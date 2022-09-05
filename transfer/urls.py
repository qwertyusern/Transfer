from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clubs/', ClubsView.as_view()),
    path('', AsosiyView.as_view()),
    path('players/', PlayersView.as_view()),
    path('u20-player/', U20PlayerView.as_view()),
    path('transfer/', TransferView.as_view()),
    path('oxirgi/', LastView.as_view()),
    path('stats/', StatsView.as_view()),
    path('urinish/', UrinishView.as_view()),
    path('about/', AboutView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)