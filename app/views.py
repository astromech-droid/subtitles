from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("app/index.html")
    message = "HelloWorld"
    context = {
        "message": message,
    }

    return HttpResponse(template.render(context, request))
