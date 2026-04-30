# Freeciv(nation) · jamaican

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/jamaican.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的jamaican定义

## 正文
```ruleset
[nation_jamaican]

name=_("Jamaican")
plural=_("?plural:Jamaicans")
groups="Modern", "American"
legend=_("Columbus landed on Jamaica in 1494. The island was colonized by\
 the Spanish but in 1655 it was conquered by the English, who turned the\
 island into a slave-based plantation economy. Slavery was abolished in\
 1834. The country became an independent country within the Commonwealth\
 in 1962. Jamaica is famous around the world for its music; genres such\
 as reggae and ska originated on the island.")

leaders = {
 "name",                        "sex"
 "Samuel Sharpe",               "Male"
 "Paul Bogle",                  "Male"
 "Alexander Bustamante",        "Male"
 "Michael Manley",              "Male"
 "P. J. Patterson",             "Male"
 "Portia Simpson-Miller",       "Female"
}

ruler_titles = {
 "government",     "male_title",            "female_title"
 "Fundamentalism", _("Rasta %s"),           _("?female:Rasta %s")
}

flag="jamaica"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "bahamian", "belizean"

cities =
 "Kingston",
 "Spanish Town",
 "Montego Bay (ocean)",
 "May Pen",
 "Port Royal (ocean)",
 "Mandeville",
 "Montego Bay (ocean)",
 "Saint Ann's Bay (ocean)",
 "Savanna la Mar (ocean)",
 "Black River",
 "Port Maria (ocean)",
 "Port Antonio (ocean)",
 "Ocho Rios",
 "Falmouth",
 "Portmore",
 "Lucea",
 "Old Harbour (ocean)",
 "Linstead",
 "Half Way Tree",
 "Bog Walk",
 "Ewarton",
 "Constant Spring",
 "Morant Bay (ocean)",
 "Hayes",
 "Old Harbour Bay (ocean)",
 "Christiana",
 "Stony Hill",
 "Santa Cruz",
 "Brown's Town",
 "Yallahs",
 "Grange Hill",
 "Bull Savanna",
 "Runaway Bay (ocean)",
 "Porus",
 "Point Hill",
 "Anotto Bay (ocean)",
 "Negril",
 "Alligator Pond"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
