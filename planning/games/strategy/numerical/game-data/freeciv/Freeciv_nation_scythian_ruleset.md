# Freeciv(nation) · scythian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/scythian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的scythian定义

## 正文
```ruleset
[nation_scythian] 

name=_("Scythian") 
plural=_("?plural:Scythians") 
groups="Ancient", "European", "Asian"
legend=_("The Scythians or Scyths were an Ancient Iranian people of\
 horse-riding nomadic pastoralists who throughout Classical Antiquity\
 dominated the Pontic-Caspian steppe, known at the time as Scythia. By\
 Late Antiquity the closely-related Sarmatians came to dominate the\
 Scythians in this area. Much of the surviving information about the\
 Scythians comes from the Greek historian Herodotus (c. 440 BCE) in his\
 Histories and Ovid in his poem of exile Epistulae ex Ponto, and\
 archaeologically from the exquisite goldwork found in Scythian burial\
 mounds in Ukraine and Southern Russia.")

leaders = {
 "name",        "sex"
 "Bartatua",    "Male"
 "Madius",      "Male"
 "Protothyes",  "Male"
 "Partitavas",  "Male"
 "Agar",        "Male"
 "Akrosas",     "Male"
 "Anacharsis",  "Male"
 "Antir",       "Male"
 "Argotes",     "Male"
 "Ariant",      "Male"
 "Ariapeith",   "Male"
 "Arimaz",      "Male"
 "Aristagoras", "Male"
 "Ateus",       "Male"
 "Gnur",        "Male"
 "Zarina",      "Female"
}

flag= "scythia" 
flag_alt = "-" 
style = "Celtic" 

init_techs="" 
init_buildings="" 
init_units="" 

conflicts_with="russian", "ukrainian", "ruthenian"
civilwar_nations="thracian", "persian", "tocharian", "ossetian", "sarmatian", "saka"

cities =
 "Tanais",
 "Kostromskaya",
 "Solocha",
 "Voronesh",
 "Shumeiko",
 "Chertomlysk",
 "Olbia",
 "Jaxartes",
 "Vettersfelde",
 "Pantikapaion",
 "Alana",
 "Sarmata",
 "Phasis",
 "Aspila",
 "Sauroma",
 "Dandaria",
 "Toreta",
 "Gorgippia",
 "Ulchu",
 "Gelonus",
 "Samarkand",
 "Aborake",
 "Sindika",
 "Kamianka",
 "Tskhinval",
 "Hermonassa",
 "Neapolis",
 "Ziwiye",
 "Orlat",
 "Solokha",
 "Histria"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
