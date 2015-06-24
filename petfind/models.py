from django.db import models
from django.utils import timezone

class CommonInfo(models.Model):
    age = models.CharField(max_length=50, verbose_name="Age", blank=True)
    breeds = models.CharField(max_length=50, verbose_name="Breeds", blank=True)
    address1 = models.CharField(max_length=50, verbose_name="Address1", blank=True)
    address2 = models.CharField(max_length=50, verbose_name="Address2", blank=True)
    city = models.CharField(max_length=50, verbose_name="City", blank=True)
    email = models.CharField(max_length=50, verbose_name="E-Mail", blank=True)
    fax = models.CharField(max_length=50,verbose_name="Fax", blank=True)
    phone = models.CharField(max_length=50, verbose_name="Phone", blank=True)
    state = models.CharField(max_length=2, verbose_name="State", blank=True)
    zip = models.CharField(max_length=5, verbose_name="Zip Code", blank=True)
    description = models.TextField(verbose_name="Description", blank=True)
    id = models.IntegerField(verbose_name="id", default=0, unique=True, primary_key=True)
    lastUpdate = models.DateTimeField(verbose_name="Date of Last Update", null=True, default=None, blank=True)
    media = models.TextField(verbose_name="Media", blank=True)
    mix = models.CharField(max_length=50, verbose_name="Mix", blank=True)
    name = models.CharField(max_length=50, verbose_name="Name", blank=True)
    options = models.CharField(max_length=50, verbose_name="Options", blank=True)
    sex = models.CharField(max_length=50, verbose_name="Sex", blank=True)
    shelterId = models.CharField(max_length=50, verbose_name="ShelterID", blank=True)
    shelterPetId = models.CharField(max_length=50, verbose_name="ShelterPetID", blank=True)
    size = models.CharField(max_length=50, verbose_name="Size", blank=True)
    status = models.CharField(max_length=50, verbose_name="Status", blank=True)

    class Meta:
        abstract = True

# Create three classes for dogs, cats, and unique
class Dog(CommonInfo):
    pass

class Cat(CommonInfo):
    pass

class Unique(CommonInfo):
    animal = models.CharField(max_length=50, verbose_name="Animal")
