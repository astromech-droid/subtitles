from django.http import HttpResponse
from django.template import loader

from app.models import Episode


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
