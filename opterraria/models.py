from django.db import models

# Create your models here.
class Npc (models.Model):
    name =models.CharField(max_length=20)
    weight=models.FloatField()
    inventory=models.CharField(max_length=200)
    enabled=models.BooleanField(default=True)
    def __str__ (self):
        return self.name + " " + str(self.weight)
class Biome (models.Model):

    name=models.CharField(max_length=20)
    features=models.CharField(max_length=200)
    enabled=models.BooleanField(default=True)

class NpcBiome (models.Model):
    bioma= models.ForeignKey(Biome,on_delete=models.CASCADE)
    npc =models.ForeignKey(Npc,on_delete=models.CASCADE)
    multiplier= models.FloatField()

class Npc_Npc (models.Model):
    npc1= models.ForeignKey(Npc,on_delete=models.CASCADE, related_name="main")
    npc2= models.ForeignKey(Npc,on_delete=models.CASCADE,related_name="neightbor")
    multiplier=models.FloatField()

class Biome_Result (models.Model):
    id_biome=models.ForeignKey(Biome,on_delete=models.CASCADE)
    id_npc = models.ForeignKey(Npc,on_delete=models.CASCADE)