from django.db import models


# Create your models here.
class Trav(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Person(models.Model):

    name1 = models.CharField(max_length=200)
    img1 = models.ImageField(upload_to='PIC')
    des1 = models.TextField()

    def __str__(self):
        return self.name1
