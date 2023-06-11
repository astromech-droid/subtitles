from django.db import models

# Create your models here.


class Episode(models.Model):
    title = models.CharField(max_length=35)

    def __str__(self):
        return self.title


class Line(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    line_number = models.IntegerField()
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text[:20]
