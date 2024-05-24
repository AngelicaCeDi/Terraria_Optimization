from django.contrib import admin

# Register your models here.
from .models import Npc, Biome, Npc_Npc, NpcBiome,Biome_Result
admin.site.register(Npc)
admin.site.register(Biome)
admin.site.register(Npc_Npc)
admin.site.register(NpcBiome)
admin.site.register(Biome_Result)
