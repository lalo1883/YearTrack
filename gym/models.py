from django.db import models


# Create your models here.

class gym_track(models.Model):
    trained_hours = models.IntegerField()
    week_number = models.IntegerField()
    trained_days = models.IntegerField()
    weight = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.trained_hours) + ' ' + str(self.week_number) + ' ' + str(self.trained_days) + ' ' + str(
            self.weight)
