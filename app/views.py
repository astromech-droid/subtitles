from django.http import HttpResponse, JsonResponse
from django.template import loader

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


def search(request):
    template = loader.get_template("app/search.html")
    context = {}

    return HttpResponse(template.render(context, request))


def search_api(request):
    regex_text: str = request.GET["regex_text"]
    lines = Line.objects.filter(text__iregex=regex_text)
    context = {"lines": []}

    for line in lines:
        context["lines"].append(_serialize_line(line))

    return JsonResponse(context)


def _serialize_line(line) -> dict:
    return {
        "text": line.serializable_value("text"),
        "timestamp": line.serializable_value("timestamp"),
        "episode_title": line.episode.title,
    }


def wordguesser(request):
    template = loader.get_template("app/wordguesser.html")
    context = {}

    return HttpResponse(template.render(context, request))


def wordguesser_api(request):
    line = Line.objects.order_by("?")[0]
    context: dict = {"line": _serialize_line(line)}

    return JsonResponse(context)
