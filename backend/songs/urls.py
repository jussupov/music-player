from django.urls import path, include
from .views import SongView

urlpatterns = [
    path('', SongView.as_view()),
]
