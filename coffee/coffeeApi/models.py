from django.db import models

# Create your models here.


# for coffee items
class Coffee(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    farm = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    fermentation = models.TextField(null=True)


    def __str__(self):
        return self.name
