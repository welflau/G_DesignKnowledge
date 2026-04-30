# Freeciv(nation) · breton

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/breton.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的breton定义

## 正文
```ruleset
[nation_breton]

name=_("Breton")
plural=_("?plural:Bretons")
groups="Medieval", "European"
legend=_("Known to the Romans as Armorica, Brittany had been Celtic\
 speaking for many centuries before Britons arrived in the peninsula as\
 mercenaries, colonists and refugees in response to the chaos in Gaul and\
 the invasion of Britain by Germanic tribes in the fifth century CE. Over\
 the centuries, use of the Breton language has been pushed towards the\
 west of the peninsula, with people speaking French instead. The Dukedom\
 of Brittany itself was formally annexed to France in 1491.")

leaders = {
 "name",        "sex"
"Frañsez I",    "Male"
"Nevenoe",      "Male"
"Alan Iañ",     "Male"
"Salaün",       "Male"
"Paskwezhen",   "Male"
"Konan II",     "Male"
"Waroch",       "Male"
"Arzhur",       "Male"
"Yann II",      "Male"
"Hawise",       "Female"
"Konstanza",    "Female"
"Anna",         "Female"
"Klaoda",       "Female"
}

ruler_titles = {
 "government", "male_title", "female_title"
 "Despotism",  _("Duke %s"), _("Duchess %s")
}

flag = "brittany"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="Cornish", "Welsh", "French"

cities =
"Roazhon", ; Rennes
"Naoned", ; Nantes
"Brest",
"Kemper", ; Quimper
"Gwened", ; Vannes
"Lannuon", ; Lannion
"Plañvour", ; Ploemeur
"Sant-Maloù", ; Saint-Malo
"Treger", ; Tréguier
"Bronn", ; Broons
"Dinan",
"Sant-Brieg", ; Saint-Brieuc
"Kallag", ; Callac
"Konk Kerne", ; Concarneau
"Felger", ; Fougères
"Lanester",
"Sant-Nazer", ; Saint-Nazaire
"An Oriant", ; Lorient
"Redon",
"Pondi", ; Pontivy
"Karnag", ; Carnac
"Gwitreg", ; Vitré
"Ankiniz", ; Ancenis
"Erdeven",
"Bangor",
"Lambaol", ; Lampaul
"Montroulez", ; Morlaix
"Kermoroc'h",
"Douar An Enez", ; Douarnenez
"Goneg", ; Gosné
"Klison", ; Clisson
"Brignogan",
"Plougastell-Daoulaz", ; Plougastel-Daoulas
"Ruca"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
