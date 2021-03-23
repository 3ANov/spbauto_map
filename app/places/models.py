from django.db import models


class Road(models.Model):
    """ Модель для хранения названия дороги """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Place(models.Model):
    """ Модель для хранения названия населённого пункта """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class County(models.Model):
    """ Модель для хранения названия округа """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StateDistrict(models.Model):
    """ Модель для хранения названия района"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
