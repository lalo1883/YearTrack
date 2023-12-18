from django.db import models

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    hours = models.FloatField()
    modules = models.IntegerField()
    link_to_course = models.CharField(max_length=100)
    date = models.DateField()


    def __str__(self):
        return self.name


class weekly_track(models.Model):
    hours_studied = models.FloatField()
    modules_studied = models.IntegerField()
    reflexions = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.reflexions