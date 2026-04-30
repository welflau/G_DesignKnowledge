# Freeciv(nation) · saka

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/saka.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的saka定义

## 正文
```ruleset
[nation_saka]

name=_("Saka")
plural=_("?plural:Saka")
groups="Ancient", "Asian"
legend=_("The Saka were an ancient Iranian tribe from the Central Asian\
 steppes. They were very closely related to the European Scythians,\
 and were probably descendants of the Andronovo culture.")
leaders = {
 "name",    "sex"
 "Skunkha", "Male"
 "Amorges", "Male"
 "Vivana",  "Male"
 "Moga",    "Male"
 "Dushana", "Male"
 "Sodasa",  "Male"
 "Vima",    "Male"
 "Arshak",  "Male"
}
flag = "saka"
flag_alt = "-"
style = "celtic"

init_techs=""
init_buildings=""
init_units=""
conflicts_with = "kazakh", "uzbek", "kyrgyz", "tajik", "afghani"
civilwar_nations = "scythian", "sarmatian", "persian", "tocharian"

cities =

"Pazyryk",
"Tagar",
"Khotan",
"Khiva",
"Gorgan",
"Bashadar",
"Tuekta",
"Ulandryk",
"Polosmak",
"Berel",
"Charklik",
"Niya",
"Jumi",
"Daha",
"Parna",
"Minusinsk",
"Uygarak",
"Issyk-Kul",
"Tushara",
"Badakhshan",
"Chitral",
"Wakhan",
"Bhullar",
"Sandhu",
"Gulcha",
"Qarategin"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
