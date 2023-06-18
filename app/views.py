from django.http import HttpResponse, JsonResponse
from django.template import loader

from app.models import Episode, Line


def index(request):
    template = loader.get_template("app/index.html")
    context = {}

    return HttpResponse(template.render(context, request))


def episodes(request):
    template = loader.get_template("app/episodes.html")
    episodes = Episode.objects.all()
    context = {"episodes": episodes}
    return HttpResponse(template.render(context, request))


def lines(request, title):
    template = loader.get_template("app/lines.html")
    episode = Episode.objects.get(title=title)
    context = {"title": title, "lines": episode.lines.all()}
    return HttpResponse(template.render(context, request))


def search(request):
    template = loader.get_template("app/search.html")
    context = {}
    return HttpResponse(template.render(context, request))


def search_api(request):
    regex = request.GET["regex"]
    lines = Line.objects.filter(text__iregex=regex).values()
    json = {"lines": list(lines)}

    return JsonResponse(json)
