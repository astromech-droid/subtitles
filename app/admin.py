from django.contrib import admin

from app.models import Episode, Line


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    list_display = ["episode", "line_number", "text"]
    pass
