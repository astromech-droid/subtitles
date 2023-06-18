from django.forms.models import model_to_dict
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
    lines = []
    regex = request.GET["regex"]
    _lines = Line.objects.filter(text__iregex=regex)

    for _line in _lines:
        line = model_to_dict(_line)
        line["title"] = _line.episode.title
        lines.append(line)

    return JsonResponse({"lines": lines})


def wordguesser(request):
    template = loader.get_template("app/wordguesser.html")
    context = {}
    return HttpResponse(template.render(context, request))


def wordguesser_api(request):
    _line = Line.objects.order_by("?")[0]
    line = model_to_dict(_line)
    line["title"] = _line.episode.title

    return JsonResponse({"line": line})
