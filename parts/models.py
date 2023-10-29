from django.db import models

# Create your models here.

class Details(models.Model):
    name = models.CharField(max_length=100)
    schema_name = models.CharField(max_length=100)
    schema_number = models.CharField(max_length=100)
    drawing_number = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    parent_components = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.name