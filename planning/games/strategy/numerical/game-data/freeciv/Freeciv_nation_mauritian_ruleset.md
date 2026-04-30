# Freeciv(nation) · mauritian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/mauritian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的mauritian定义

## 正文
```ruleset
[nation_mauritian]

name = _("Mauritian")
plural = _("?plural:Mauritians")
groups="African", "Modern"
legend=_("Mauritius is an island in the Indian Ocean. It was first settled\
 by the Dutch, who named it after Maurice of Nassau. The island is famous\
 for being the habitat of the dodo, which was was brought to extinction\
 within a century after its discovery. The Dutch abandoned the island in\
 1710 and Mauritius was subsequently settled by the French. During the\
 Napoleonic Wars the island was captured by the British. The island\
 became independent in 1968. Nowadays, Mauritius is one of the most\
 developed countries of Africa. The population is mostly of Indian,\
 African and European origin.")

leaders = {
 "name",                                     "sex"
 "Adriaen van der Stel",                     "Male"
 "Bertrand-François Mahé de La Bourdonnais", "Male"
 "Robert Townsend Farquhar",                 "Male"
 "Maurice Cure",                             "Male"
 "Seewoosagur Ramgoolam",                    "Male"
 "Cassam Uteem",                             "Male"
}

flag = "mauritius"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="malagasy", "seychellois"

cities =
 "Port Louis",
 "Beau Bassin-Rose Hill",
 "Centre de Flacq",
 "Triolet",
 "Mahébourg",
 "Poude d'Or",
 "Quartier Militaire",
 "Bambous",
 "Souillac",
 "Port Mathurin",
 "Vacoas-Phoenix",
 "Pamplemousse",
 "Moka",
 "Curepipe",
 "Quatre Bornes",
 "Goodlands",
 "Rivière Sèche",
 "Saint Pierre",
 "Lataniers-Mont Lubin",
 "Le Hochet",
 "Baie du Tombeau",
 "Rose Belle",
 "Chemin Grenier",
 "Riviere du Rempart",
 "Grand Baie",
 "Plaine Magnien",
 "Pailles",
 "Petit Gabriel",
 "Lalmatie",
 "Surinam",
 "New Grove",
 "Rivière des Anguilles",
 "Terre Rouge",
 "Petit Raffray",
 "Montagne Blanche",
 "L'Escalier",
 "Rivière Cocos",
 "Long Mountain",
 "Plaines des Papaues",
 "Grand Bois",
 "Pointe aux Piments",
 "Brisee Verdiere",
 "Medine-Camp de Masque",
 "Nouvelle France",
 "Poste de Flacq",
 "Vingt Cinq",
 "Grand Gaube",
 "Beau Vallon",
 "Raphael"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
