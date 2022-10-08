from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import *

router = DefaultRouter()
router.register(r"genre", views.GenreViewSet, basename="genre")
router.register(r"movie", views.MovieViewSet, basename="movie")
router.register(r"title", views.TitleSearchView, basename="title")

urlpatterns = [
    path("", include(router.urls)),
    ]
