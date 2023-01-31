from django.db import models


# Create your models here.
class Trav(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Person(models.Model):

    people = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='persons')
    words = models.TextField()

    def __str__(self):
        return self.people
