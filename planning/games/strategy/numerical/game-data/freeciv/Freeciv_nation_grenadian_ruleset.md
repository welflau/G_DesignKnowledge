# Freeciv(nation) · grenadian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/grenadian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的grenadian定义

## 正文
```ruleset
[nation_grenadian]

name=_("Grenadian")
plural=_("?plural:Grenadians")
groups="American", "Modern"
legend=_("Grenada is an island nation in the Caribbean. It gained\
 independence from the United Kingdom in 1974. The main island was known\
 as Camahogne by the indigenous Caribs.")

leaders = {
 "name",                "sex"
 "Eric Gairy",          "Male" ; First Prime Minister.
 "Maurice Bishop",      "Male" ; New Jewel Movement.
 "Bernard Coard",       "Male" ; Army coup.
 "Phyllis Coard",       "Female" ; Army coup.
 "Herbert Blaize",      "Male" ; Founder of GNP.
}

ruler_titles = {
 "government",      "male_title",   "female_title"
 "Fundamentalism",  _("Bishop %s"), _("?female:Bishop %s")
}

flag="grenada"
flag_alt = "united_kingdom"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "vincentian"

cities =
 "St. George's",	; Previously known as Fort Royal
 "Grenville",
 "Gouyave",
 "Hillsborough",
 "Hence",
 "North Village",
 "Grand Bay",
 "Victoria",
 "Marquis",
 "Sauteurs",
 "Calivigny",
 "Grand Roy",
 "Diego Piece",
 "Upper Pearl",
 "Simon",
 "Chutz",
 "Mamma Cannes",
 "Beaton",
 "Morne",
 "Lance aux Epines",
 "Morne Docteur",
 "Mabouya",
 "Argyle",
 "Lovell",
 "Barbruce",
 "Old Wall",
 "Mt Royal",
 "Glossy",
 "Retreat",
 "L'Ance Guyac",
 "Cheltenham",
 "Ashton",
 "L'Appelle"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
