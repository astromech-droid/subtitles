from django.db import models


class Episode(models.Model):
    title = models.CharField(max_length=35)

    def __str__(self):
        return self.title


class Line(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    line_number = models.IntegerField()
    timestamp = models.TimeField(null=True)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text[:20]
