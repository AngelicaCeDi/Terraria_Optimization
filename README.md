# Terraria_Optimization

This project aims to share an optimization model for terraria npc housing.

You can enable or disable every biome, npc, and also edit the NPC weight to maximize the discount rate

## NPC happiness input data

![npc_data](https://static.wikia.nocookie.net/terraria_gamepedia/images/c/c0/Happiness_chart.png/revision/latest?cb=20230523013148)

## Database structure

NPC  
1. id_npc (pk, int)
2. Name (string)
3. Weight (float)
4. Inventory (string)
5. Enabled (bool)

Biome
1. id_biome (pk, int)
2. Name (string)
3. Features (string)
4. Enabled (bool)

bioma_npc
1. id_biome_npc (pk, int)
2. bioma (fk, int)
3. npc (fk, int)
4. multiplier (float)

npc_npc
1. id_npc_npc (pk, int)
2. id_npc1 (fk, int)
3. id_npc2 (fk, int)
4. multiplier (float)

biome_result
1. id_res (pk, int)
2. id_biome (fk, int)
3. id_npc (fk, int)

npc_result *WIP*

## Happines calculation

$H_n = F_{b,n} \cdot \prod_{m | m \in b} L_{n,m}$

The hapiness of and npc is equal to the biome factor which the NPC is, time the productory of the NPC that are living with.

PS: For simplication, and in order to make a linear modelo, we are going to transfor the productory as a summation