# Freeciv(nation) · scanian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/scanian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的scanian定义

## 正文
```ruleset
[nation_scanian]

name=_("Scanian")
plural=_("?plural:Scanians")
groups="Medieval", "European"
legend=_("Scania is the southernmost region of Sweden. Historically one of\
 many petty kingdoms in Viking age Scandinavia, it became in medieval times\
 part of Denmark but was ceded to Sweden through the Treaty of Roskilde in\
 1658. Scania saw something of a national revival in the late 20th century\
 with calls for greater autonomy within the Kingdom of Sweden.")

leaders = {
 "name",             "sex"
 "Skalk",            "Male"
 "Ingjald Frodesøn", "Male"
 "Attilla Skåning",  "Male"
 "Hottar",           "Male"
 "Hjorvald Ylfing",  "Male"
 "Ostmar",           "Male"
 "Halfdan Snjalli",  "Male"
 "Ale den Frøkne",   "Male"
}

ruler_titles = {
 "government",   "male_title",           "female_title"
 "Despotism",    _("Earl %s"),           _("?female:Earl %s")
}

flag="scania"
flag_alt="-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Danish" ; Similar flag
civilwar_nations="Swedish"

; Cities in Skåne unless otherwise noted
; Danish/Scanian forms with Swedish in comment
cities =
 "Lindholm (ocean)", ; Lindholmen
 "Luntertun",
 "Væ", ; Vä
 "Hven", ; Ven
 "Tommerup", ; Tumathorp
 "Villand",
 "Åsbo",
 "Gønge", ; Göinge
 "Gers", ; Gärds
 "Albo",
 "Onsø", ; Onsjö
 "Frosta",
 "Fers", ; Färs
 "Rønnebjerg (mountains, hills)", ; Rönneberg
 "Harriager", ; Harjager
 "Oxie",
 "Torna",
 "Bara",
 "Vemmenhøj (hills)", ; Vemmenhög
 "Herrested", ; Herrestad
 "Ingelsted", ; Ingelstad
 "Jerrested", ; Järrestad
 "Åhus",
 "Opager", ; Uppåkra
 "Dalby",

; Greater Skåneland
 "Beridsholm (ocean)",
 "Falsterbo",
 "Falkenberg (mountains, hills)", ; in Halland
 "Simrishamn (ocean)",
 "Sølvesborg", ; Sölvesborg, Blekinge
 "Helsingborg",
 "Visborg", ; in Gotland
 "Halmstad", ; in Halland
 "Hammershus", ; Bornholm, Denmark
 "Lykkeby", ; Lyckå, Blekinge
 "Christiansstad", ; Kristianstad
 "Landskrone", ; Landskrona
 "Laholm (ocean)", ; in Halland
 "Varberg (mountains, hills)", ; in Halland
 "Lundegård",
 "Næsbyholm (ocean)", ; Näsbyholm
 "Malmøhus", ; Malmöhus
 "Arnsborg" ; in Saaremaa, Estonia

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
