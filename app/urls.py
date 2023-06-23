from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("episodes/", views.episodes, name="episodes"),
    path("episodes/<title>/", views.episode, name="episode"),
    path("episodes/<title>/<line_number>/", views.episode, name="episode_line"),
    path("api/episodes/<title>/", views.episode_api, name="episode_api"),
    path("api/episodes/<title>/<line_number>/", views.line_api, name="line_api"),
    path("search/", views.search, name="search"),
    path("wordguesser/", views.wordguesser, name="wordguesser"),
    path("api/search/", views.search_api, name="search_api"),
    path("api/wordguesser/", views.wordguesser_api, name="wordguesser_api"),
]
