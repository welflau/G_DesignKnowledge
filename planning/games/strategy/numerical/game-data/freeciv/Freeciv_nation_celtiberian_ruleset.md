# Freeciv(nation) · celtiberian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/celtiberian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的celtiberian定义

## 正文
```ruleset
[nation_celtiberian]

name=_("Celtiberian")
plural=_("?plural:Celtiberians")
groups="Ancient", "European"
legend=_("The Celtiberians were a people from East-Central Spain that lived\
 during the last millennium BCE. They were of mixed Celtic and Iberian\
 descent and were defeated by Rome in the Numantian War.")

leaders = {
 "name",        "sex"
 "Avaro",       "Male"
 "Indortes",    "Male"
 "Istolakio",   "Male"
 "Leukon",      "Male"
 "Magavariko",  "Male"
 "Olindiko",    "Male"
 "Pirreso",     "Male"
 "Retogenes",   "Male"
 "Thurro",      "Male"
}

flag="celtiberian"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""
conflicts_with = "spanish", "castilian", "catalan", "aragonese"
civilwar_nations = "iberian", "gallic", "gaelic"

cities =
 "Numantia",
 "Okilis",
 "Titom",
 "Turiaso",
 "Kontebakom",
 "Sekaisa",
 "Kluniako",
 "Nertobriga",
 "Tiermes",
 "Kontrebia Karbika",
 "Aratikos",
 "Kalakorikos",
 "Segobriga",
 "Titiacos",
 "Uxama Argaela",
 "Burzao",
 "Lonimbriga",
 "Karauez",
 "Deobriga",
 "Kontrebia Leukade",
 "Kemelon",
 "Lutia",
 "Kontrebia Belaisca",
 "Erkavika",
 "Eberobriga",
 "Laminiom",
 "Nertobriga",
 "Konsabura",
 "Talabriga",
 "Uarakos",
 "Komplega",
 "Karavis",
 "Iplakea"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
