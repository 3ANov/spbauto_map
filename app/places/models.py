from django.db import models

# Create your models here.


class Road(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StateDistrict(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
