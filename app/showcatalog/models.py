from django.db import models

# Create your models here.


class Show(models.Model):
    name = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    age_rating = models.CharField(max_length=255)
