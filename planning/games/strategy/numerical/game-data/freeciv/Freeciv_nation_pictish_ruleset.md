# Freeciv(nation) · pictish

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/pictish.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的pictish定义

## 正文
```ruleset
[nation_pictish]

name = _("Pictish")
plural = _("?plural:Picts")
groups="European", "Ancient", "Medieval"
legend=_("The Picts were the indigenous inhabitants of Caledonia, Ancient\
 Scotland. They were probably Celtic or maybe Celticized pre-Indo-Europeans.\
 They were given the name Picts, \'painted people\', by the Romans because of\
 their custom of tattooing their bodies. The Picts survived until well into\
 the Middle Ages but by the 11th century they had been assimilated by the\
 Gaelic Scots.")
leaders = {
 "name",     "sex"
 "Drest",    "male"
 "Bridei",   "male"
 "Der-Ilei", "female"
 "Nechtan",  "male"
 "Eogan",    "male"
 "Ciniod",   "male"
}

ruler_titles = {
 "government",     "male_title",       "female_title"
 "Anarchy",        _("Usurper %s"),    _("?female:Usurper %s")
 "Fundamentalism", _("Druid %s"),      _("?female:Druid %s")
 "Monarchy",       _("High King %s"),  _("High Queen %s")
} 

flag = "pict"
flag_alt = "scotland"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="scottish"
civilwar_nations="gaelic", "briton", "scottish"

cities =
 "Circinn",
 "Fotla",
 "Fortriu",
 "Cait",
 "Ce",
 "Fib",
 "Fidach",
 "Dumna",
 "Orcas",
 "Inchtuthil",
 "Devana",
 "Alauna",
 "Peanfahel",
 "Lindon",
 "Coria",
 "Colania",
 "Pitmedden",
 "Vanduara",
 "Alcluith",
 "Corda",
 "Rerigonion",
 "Locopibia",
 "Lanbride",
 "Fannaguchti",
 "Mar",
 "Dundurn"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
