from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    mailing_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    course = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    reason_to_join = models.CharField(max_length=200)
    checklist = models.CharField(max_length=200)
    agree_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.name
