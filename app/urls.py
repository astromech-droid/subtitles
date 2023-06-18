from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("episodes/", views.episodes, name="episodes"),
    path("episodes/<title>/", views.lines, name="lines"),
    path("search/", views.search, name="search"),
    path("api/search/", views.search_api, name="search_api"),
]
