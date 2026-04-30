# Freeciv(nation) · helvetian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/helvetian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的helvetian定义

## 正文
```ruleset
[nation_helvetian]

name=_("Helvetian")
plural=_("?plural:Helvetians")
groups="Ancient", "European"
legend=_("The Helvetians (Latin: Helvetii) were an Ancient Celtic people,\
 inhabiting what is now Switzerland and adjacent parts of France and\
 Germany. Helvetians sometimes helped in the internal conflicts of Rome,\
 for example, on the side of Cicero. They were a big, expansive tribe,\
 striving for domination over the tribes of Gaul. The campaigns of the\
 Helvetian chieftain Orgetorix were used by Caesar as a pretext to\
 conquer Helvetia and the rest of Gaul. The Helvetians succumbed to the\
 Romans and became Romanized during the following centuries.")
leaders = {
 "name",                "sex"
 "Orgetorix",           "Male"
 "Divico",              "Male"
 "Dumnotauros",         "Male"
 "Nammeios",            "Male"
 "Verucloitios",        "Male"
 "Caburos",             "Male"
}
flag="helvetii"
flag_alt = "-"
style = "Celtic"

ruler_titles = { "government",      "male_title",       "female_title"
                 "Despotism",       _("Chieftain %s"),  _("?female:Chieftain %s")
                 "Fundamentalism",  _("High Druid %s"), _("?female:High Druid %s")
               }

init_techs=""
init_buildings=""
init_units=""

conflicts_with="swiss", "french", "badian", "wuerttembergian", "burgundian"
civilwar_nations="Gallic" ;Boian, Belgic

cities =
 "Aventicum",
 "Brenodurum",
 "Basilea",
 "Genava",
 "Lousonna",
 "Octodurus",
 "Vindonissa",
 "Vesontio",
 "Uimpina",
 "Cambioratin",
 "Urba",
 "Noviodunum",
 "Minnodunum",
 "Augaunum",
 "Lousodunum",
 "Viviscus",
 "Arialbinnum",
 "Pennelucos",
 "Epamanduodurum",
 "Larga",
 "Tasgaetium",
 "Ariolica",
 "Tenedo",
 "Eburodunum",
 "Tarnaiae",
 "Vitodurum",
 "Uromagus",
 "Iuliomagus",
 "Salodurum",
 "Petinesca",
 "Cambete",
 "Vocetius",
; Other settlements of Helveti
 "Eppenberg",
 "Jensberg",
 "Bois de Chatel",
 "Altenburg-Rheinau",
 "Uetliberg",
 "Sermuz",
 "Mont Vully",
 "Mont Terri",
 "Mont Chaibeuf"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
