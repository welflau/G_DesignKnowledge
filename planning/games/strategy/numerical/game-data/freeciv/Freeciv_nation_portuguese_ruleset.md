# Freeciv(nation) · portuguese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/portuguese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的portuguese定义

## 正文
```ruleset
[nation_portuguese]

translation_domain="freeciv"

name=_("Portuguese")
plural=_("?plural:Portuguese")
groups="Medieval", "Early Modern", "Modern", "European", "Core"
legend=_("Portugal founded the first of the great mercantile empires\
 in the 1400s on the shipbuilding advances funded by Prince Henry the\
 Navigator.")

leaders = {
 "name",                        "sex"
 "Afonso Henriques",            "Male"
 "Sancho I",                    "Male"
 "Dinis",                       "Male"
 "Afonso IV",                   "Male"
 "João I",                      "Male"
 "João II",                     "Male"
 "Manuel I",                    "Male"
 "João IV",                     "Male"
 "Maria II",                    "Female"
 "António de Oliveira Salazar", "Male"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Despotism",       _("Viscount %s"),       _("Viscountess %s")
 "Fundamentalism",  _("Patriarch %s"),      _("Mother Superior %s")
}

flag="portugal"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "brazilian", "angolan",  "bissau-guinean", "cape verdean",
 "east timorese", "mozambican", "santomean"


cities =
 "Lisboa",
 "Guimarães",
 "Guarda",
 "Vila Real",
 "Viseu",
 "Braga",
 "Porto (ocean)",
 "Coimbra",
 "Aveiro",
 "Leiria",
 "Bragança",
 "Barcelos",
 "Sintra",
 "Setúbal",
 "Alcácer do Sal",
 "Santarém",
 "Silves",
 "Évora",
 "Portalegre (ocean)",
 "Faro",
 "Elvas",
 "Óbidos",
 "Alcobaça",
 "Alcochete",
 "Alcoutim",
 "Tomar",
 "Alenquer",
 "Aljubarrota",
 "Fátima",
 "Batalha",
 "Nazaré",
 "Aljustrel",
 "Almada",
 "Almeirim",
 "Aljezur",
 "Odemira",
 "Viana do Castelo (mountains)",
 "Chaves",
 "Castelo Branco (mountains)",
 "Caldas da Rainha",
 "Estremoz",
 "Vila Viçosa",
 "Sines",
 "Portimão",
 "Albufeira",
 "Lagos",
 "Tavira",
 "Marvão",
 "Mafra",
 "Palmela",
 "Cascais",
 "Estoril",
 "Funchal",
 "Ponta Delgada",
 "Torres Vedras",
 "Torres Novas",
 "Amadora",
 "Queluz",
 "Maia",
 "Figueira da Foz (river)",
 "Matosinhos",
 "Vila Nova de Gaia"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
