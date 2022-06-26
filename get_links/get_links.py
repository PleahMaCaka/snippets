import clipboard

# noinspection SpellCheckingInspection
text = """
Goblins_Dungeons_1.0.8.jar: https://www.curseforge.com/minecraft/mc-mods/goblins-dungeons/download/3785691
hexerei-0.1.19.jar: https://www.curseforge.com/minecraft/mc-mods/hexerei/download/3785792
alexsdelight-1.18.2-1.2.3.jar: https://www.curseforge.com/minecraft/mc-mods/alexs-delight/download/3787817
Gobber_Delight_1.0.1_Forge_1.18.2.jar: https://www.curseforge.com/minecraft/mc-mods/gobber-delight-a-farmers-delight-add-on/download/3796583
Illager Plushies 1.1.5 1.18.2.jar: https://www.curseforge.com/minecraft/mc-mods/illager-plushies/download/3797857
mcwfencesbyg-1.18.2-1.1.jar: https://www.curseforge.com/minecraft/mc-mods/macaws-fences-oh-the-biomes-youll-go/download/3829564
fancymenu_forge_2.8.0_MC_1.18.2.jar: https://www.curseforge.com/minecraft/mc-mods/fancymenu-forge/download/3833651
eccentrictome-1.18.2-1.6.0.jar: https://www.curseforge.com/minecraft/mc-mods/eccentric-tome/download/3835270
"""

sp = text.replace("\n", " ").split(" ")
links = []
one_line = ""

for e in sp:
    if e.startswith("https://") or e.startswith("http://"):
        links.append(e)

for link in links:
    one_line += link + " "

clipboard.copy(one_line)

print(one_line)
