# Freeciv(nation) · guyanese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/guyanese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的guyanese定义

## 正文
```ruleset
[nation_guyanese]

name=_("Guyanese")
plural=_("?plural:Guyanese")
groups="American", "Modern"

legend=_("Originally inhabited by the Arawk, Guyana was colonized by the\
 Dutch but became a British colony after the Napoleonic Wars. It gained\
 independence in 1966. Under Forbes Burnham Guyana became a Marxist\
 oriented country, but in the 1980s it started its transition to a market\
 democracy.")

leaders = {
 "name",                        "sex"
 "Cuffy",                       "Male"
 "Gordon James Lethem",         "Male"
 "Forbes Burnham",              "Male"
 "Cheddi Jagan",                "Male"
 "Janet Rosenberg Jagan",       "Female"
 "Bharrat Jagdeo",              "Male"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Communism",       _("Chairman %s"),       _("Chairwoman %s")
 "Fundamentalism",  _("Reverend %s"),       _("?female:Reverend %s")
 "Republic", _("Executive President %s"),_("?female:Executive President %s")
}

flag="guyana"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="venezuelan", "surinamese", "trinidadian and tobagonian"

cities =
 "Georgetown",
 "Linden",
 "New Amsterdam",
 "Bartica",
 "Corriverton",
 "Rosignol",
 "Mahaica",
 "Ituni",
 "Skeldon",
 "Paradise",
 "Vreed en Hoop",
 "Fort Wellington",
 "Mahaicony",
 "Kumaka",
 "Anna Regina",
 "Mabaruma",
 "Lethem",
 "Soesdyke",
 "Orinduik",
 "Kato",
 "Rustenburg",
 "Fort Nassau",
 "Kyk-over-al",
 "Kurupukari",
 "Puerto Turumbán",
 "Morawhanna",
 "Crabwood Creek",
 "Juçara",
 "Hackney",
 "Marlborough",
 "Golden Fleece",
 "Spring Garden",
 "Kartabu",
 "Winepuru",
 "Rockstone",
 "Urisirima",
 "Mora",
 "Parika",
 "Jonestown",
 "Potosi",
 "Sand Hills",
 "Elizabeth",
 "Christianburg",
 "Labba",
 "Lusignan",
 "Clonbrook",
 "Mahaica Helena",
 "Rosignol",
 "Laluni",
 "Highbury",
 "Alness",
 "Leeds",
 "Waiwai",
 "Five Stars"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
