# Freeciv(nation) · mapuche

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/mapuche.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的mapuche定义

## 正文
```ruleset
[nation_mapuche]

name=_("Mapuche")
plural=_("?plural:Mapuche")
groups="American", "Early Modern"

legend=_("The Mapuche people successfully resisted the expansion of the Inka\
 empire, halting them at the Maule river in what is now central Chile. They\
 proved to be stubborn opponents of the Spanish, too, who, along with their\
 Chilean successors, took 300 years to conquer them.")

leaders = {
 "name",        "sex"
 "Lef-Traru",   "Male"
 "Caupolicán",  "Male"
 "Colocolo",    "Male"
}

flag         = "mapuche"
flag_alt     = "-"
style        = "Celtic"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "inca", "chilean"

cities =
 "Tucapel",
 "Temuco",
 "Purén",
 "Lebu",
 "Angol",
 "Collipulli",
 "Lonquimay",
 "Ercilla",
 "Traiguén",
 "Lumaco",
 "Curacautin",
 "Marihueñu",
 "Tolhuaca",
 "Lonquimay",
 "Llaima",
 "Malleco",
 "Malalcahuello",
 "Carahue",
 "Pillánlelbu",
 "Pucón",
 "Mulchén",
 "Itata",
 "Toltén",
 "Yungay",
 "Chillán",
 "Ñiquén",
 "Ránquil"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
