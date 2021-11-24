from django.contrib import admin
from django.urls import path
from song.views import get_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('song/', get_all),
]
