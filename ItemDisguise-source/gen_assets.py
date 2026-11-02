import json, os
base = "src/main/resources/assets/minecraft"

def w(path, data):
    p = os.path.join(base, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        json.dump(data, f, indent=2)

# item look (what you see in inventory / hand)
items = {
    "blue_glazed_terracotta": "minecraft:item/elytra",
    "slime_ball": "minecraft:block/ancient_debris",
    "heavy_weighted_pressure_plate": "minecraft:block/spawner",
    "sea_lantern": "minecraft:block/netherite_block",
    "wither_rose": "minecraft:item/mace",
    "sticky_piston": "minecraft:block/gilded_blackstone",
}
for k, m in items.items():
    w("items/%s.json" % k, {"model": {"type": "minecraft:model", "model": m}})

# placed block look
blocks = {
    "heavy_weighted_pressure_plate": "minecraft:block/spawner",
    "sea_lantern": "minecraft:block/netherite_block",
    "sticky_piston": "minecraft:block/gilded_blackstone",
}
for k, m in blocks.items():
    w("blockstates/%s.json" % k, {"variants": {"": {"model": m}}})

# names
w("lang/en_us.json", {
    "block.minecraft.blue_glazed_terracotta": "Elytra",
    "item.minecraft.slime_ball": "Ancient Debris",
    "block.minecraft.heavy_weighted_pressure_plate": "Skeleton Spawner",
    "block.minecraft.sea_lantern": "Netherite Block",
    "block.minecraft.wither_rose": "Mace",
    "block.minecraft.sticky_piston": "Gilded Blackstone",
})
print("assets written")
