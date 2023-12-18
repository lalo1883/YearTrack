from django.db import models

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    rating = models.FloatField()
    pages = models.IntegerField()

    def __str__(self):
        return self.name

class weekly_track(models.Model):
    hours_read = models.FloatField()
    pages_read = models.IntegerField()
    reflexions = models.TextField()
