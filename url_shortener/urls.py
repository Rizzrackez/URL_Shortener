from django.contrib import admin
from django.urls import path, include

from url_shortener.views import custom404

handler404 = custom404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("shortener_app.urls")),
]
