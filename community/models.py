from django.db import models
from django.contrib.auth.models import User

class Party(models.Model):
    party_name = models.CharField(max_length=20, unique=True)
    party_leader = models.CharField(max_length=35, unique=False)

    def __str__(self):
        return self.party_name + " , " + self.party_leader


class Constituency(models.Model):
    constituency_name = models.CharField(max_length=70, unique=True)
    constituency_MP = models.CharField(max_length=50, unique=False)
    party_holding = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="holds")

    def __str__(self):
        return self.constituency_name + "," + self.constituency_MP + "," + self.party_holding.party_name
    

# Create your models here.
