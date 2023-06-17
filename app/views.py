from django.http import HttpResponse, JsonResponse
from django.template import loader

from app.models import Line


def index(request):
    template = loader.get_template("app/index.html")
    message = "HelloWorld"
    context = {
        "message": message,
    }

    return HttpResponse(template.render(context, request))


def search(request):
    regex = request.GET["regex"]
    lines = Line.objects.filter(text__iregex=regex).values()
    json = {"lines": list(lines)}

    return JsonResponse(json)
