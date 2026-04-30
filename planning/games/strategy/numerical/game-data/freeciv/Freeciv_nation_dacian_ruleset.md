# Freeciv(nation) · dacian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/dacian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的dacian定义

## 正文
```ruleset
[nation_dacian]

name=_("Dacian")
plural=_("?plural:Dacians")
groups="Ancient", "European"
legend=_("The Dacians were ancient tribes who lived on the left bank of\
 the Lower Danube in Dacia in what is now Romania. They were probably\
 related to the Thracians and other Paleo-Balkanic tribes. The unification\
 of Dacian tribes occurred during the reign of king Burebista. After the\
 wars with Rome, they were defeated in 106 CE. Dacia became a Roman\
 province and succumbed to Roman colonization. The remains of the Dacians\
 mingled with East Germanic tribes and later with Slavs.")
leaders = {
 "name",                "sex"
 "Kothelas",            "Male"
 "Remaksos",            "Male"
 "Moskon",              "Male"
 "Dromikhaites",        "Male"
 "Zalmodegikos",        "Male"
 "Rubobostes",          "Male"
 "Dikomes",             "Male"
 "Kotiso",              "Male"
 "Zyrakses",            "Male"
 "Burebista",           "Male"
 "Skorillo",            "Male"
 "Dekebalos",           "Male"
}
flag="dacian"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Romanian", "Moldovan", "Transylvanian", "Ukrainian",
               "Hungarian", "Bulgarian", "Serbian", "Yugoslav"
civilwar_nations = "Thracian", "Scythian", "Illyrian"

cities =
"Sarmizegetusa",
"Argedava",
"Marcodava",
"Desudaba",
"Capidava",
"Carsidava",
"Drobeta",
"Malva",
"Petrodava",
"Napoca",
"Polonda",
"Potaissa",
"Arutela",
"Buteridava",
"Arcobadara",
"Genucla",
"Dausdava",
"Dinogetia",
"Giridava",
"Pulpudeva",
"Kuimedaba",
"Piroboridava",
"Sagadava",
"Ramidava",
"Scaidaba",
"Tapai",
"Tirista",
"Singidava",
"Zeugma",
"Zurobara",
"Utidava",
"Setidava",
"Zaldapa",
"Setidava",
"Klepidava",
"Zurobara",
"Dierna",
"Susudava",
"Nentinava",
"Itadeba",
"Buridava",
"Danedebai",
"Bregedaba",
"Germidava"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
