# Freeciv(nation) · burgundic

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/burgundic.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的burgundic定义

## 正文
```ruleset
[nation_burgundic]

name=_("Burgundic")
plural=_("?plural:Burgunds")
groups="Ancient", "European"
legend=_("The Burgundians were an ancient East Germanic people who\
 probably originated on Bornholm island. After leaving Bornholm they\
 lived between the Oder and Vistula rivers. During the Migration Period,\
 along with other Germanic peoples they invaded the Roman Empire, and in\
 472 CE, some of them sacked Rome. Their first kingdom was founded in\
 Worms, but after its destruction by the Huns they moved to what is today\
 Savoy and Burgundy, where they founded their second kingdom.\
 Eventually they were subordinated by the Frankish Kingdom. The Burgundians\
 gave their name to the later Romance nation and region of Burgundy.")
leaders = {
 "name",                "sex"
 "Brunhild",            "Female"
 "Gebikka",             "Male"
 "Gislahar",            "Male"
 "Gundahar",            "Male"
 "Gundiok",             "Male"
 "Gundobad",            "Male"
 "Chilperik II",        "Male"
 "Clotild",             "Female"
 "Sigismund",           "Male"
 "Godomar",             "Male"
}
flag="burgundic"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Burgundian", "French", "Swiss", "Savoyard"
civilwar_nations = "Frankish", "Ostrogothic", "Visigothic", "Western Roman" ; Alemannic

cities =
 "Borbetomagus",            ;Wormatia, Worms
 "Moguntiacum",             ;Mainz
 "Lugdunum",                ;Lyon
 "Vienna",                  ;Vienne
 "Valentia",                ;Valence
 "Vesontio",                ;Besançon
 "Darantasia",              ;Tarantaise 
 "Genava",                  ;Genéve
 "Octodurus",               ;Martigny
 "Augustodunum",            ;Autun
 "Eburodunum",              ;Embrun
 "Divio",                   ;Dijon
 "Lausona",                 ;Lausanne
 "Sedunum",                 ;Sion
 "Augusta Praetoria",       ;Aosta
 "Basilia",                 ;Basel
 "Dola",                    ;Dole
 "Gratianopolis",           ;Grenoble
 "Cluniacum",               ;Cluny
 "Cabillonum",              ;Chalon-sur-Saône
 "Brigantium",              ;Briançon
 "Ariolica",                ;Pontarlier
 "Aventicum",               ;Avenches
 "Argentoratum",            ;Strasbourg
 "Arelate",                 ;Arles
 "Spira",                   ;Speyer
 "Autessiodurum",           ;Auxerre
 "Lingones",                ;Langres
 "Avennio",                 ;Avignon
 "Arausio",                 ;Orange
 "Vivisco",                 ;Vevey
 "Acaunus",                 ;Saint-Maurice
 "Nivernum",                ;Nevers
 "Tullum",                  ;Toul
 "Salodurum",               ;Solothurn
 "Veseruntia"               ;Vézeronce

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
