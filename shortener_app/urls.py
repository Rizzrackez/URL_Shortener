from django.urls import path

from shortener_app.views import SourceUrlCreateView, SourceUrlListView, browse_source_url_view
from url_shortener.views import custom404

handler404 = custom404

urlpatterns = [
    path('', SourceUrlListView.as_view()),
    path('create_url_shorterer/', SourceUrlCreateView.as_view()),
    path('<str:slug>/', browse_source_url_view),
]
