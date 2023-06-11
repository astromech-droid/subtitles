import re

from django.db import models

# Create your models here.


class Episode(models.Model):
    title = models.CharField(max_length=35)

    def __str__(self):
        return self.title

    def import_txt(self, path: str):
        with open(path, "r") as f:
            lines = f.readlines()
            entries = []

            for i, line in enumerate(lines, 1):
                _match = re.match(r"^(\d{2}:\d{2}:\d{2})\.\d{3}: (.*)$", line.strip())
                entry = Line(
                    episode=self,
                    line_number=i,
                    timestamp=_match[1],
                    text=_match[2],
                )
                entries.append(entry)

        lines = Line.objects.bulk_create(entries)

        return lines


class Line(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    line_number = models.IntegerField()
    timestamp = models.TimeField(null=True)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text[:20]
