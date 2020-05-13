from django.db import models
from django.utils import timezone




class Pet(model.Models):
    pet_name = models.Charfield(max_length=200)
    species = models.Charfield(max_length=200)
    breed = models.Charfield(max_length=200)
    weight_in_pounds = models.IntegerField(default=0)
    #
    owner= models.ForeignKey(Owner,blank=NONE)

class Appointment(models.Models):
    #
    date_of_apointment = models.DateTimeField()
    durtation_minutes = models.IntegerField(default=0)
    special_instructions = models.CharField(max_length=200)
    pet = models.ForeignKey(Pet)


class Owner(models.Model):
    owenr_name= models.Charfield(max_length=200)
    



  