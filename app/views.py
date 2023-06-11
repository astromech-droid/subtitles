import os

from django.http import HttpResponse
from django.template import loader
from subtitles import settings

from app.models import Episode, Line


def index(request):
    template = loader.get_template("app/index.html")
    episodes = Episode.objects.all()
    context = {"episodes": episodes}

    return HttpResponse(template.render(context, request))


def episodes(request):
    template = loader.get_template("app/episodes.html")
    episodes = Episode.objects.all()
    context = {"episodes": episodes}

    return HttpResponse(template.render(context, request))


def lines(request, title):
    template = loader.get_template("app/lines.html")
    episode = Episode.objects.get(title=title)
    lines = Line.objects.filter(episode=episode)
    context = {"lines": lines}

    return HttpResponse(template.render(context, request))
