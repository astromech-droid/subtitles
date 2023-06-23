import json

from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

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


def episode(request, title, line_number=0):
    template = loader.get_template("app/lines.html")
    episode = Episode.objects.get(title=title)
    context = {
        "title": title,
        "lines": episode.lines.all(),
        "line_number": int(line_number),
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def episode_api(request, title):
    if request.method == "POST":
        entries = []
        episode = Episode.objects.get_or_create(title=title)
        body = json.loads(request.body.decode("utf-8"))

        lines = body["lines"]
        line_count = episode[0].lines.count()

        for i, line in enumerate(lines, line_count + 1):
            timestamp, text = line
            entries.append(
                Line(episode=episode[0], timestamp=timestamp, text=text, line_number=i)
            )

        Line.objects.bulk_create(entries)

        return HttpResponse(status=201)


def line_api(request, title, line_number):
    episode = Episode.objects.get(title=title)
    _line = Line.objects.filter(episode=episode).get(line_number=line_number)
    line = model_to_dict(_line)
    line["title"] = episode.title

    return JsonResponse({"line": line})


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
    _line = (
        Line.objects.filter(~Q(text__endswith="]"))
        .filter(~Q(text__endswith=")"))
        .order_by("?")
        .first()
    )
    line = model_to_dict(_line)
    line["title"] = _line.episode.title

    return JsonResponse({"line": line})
