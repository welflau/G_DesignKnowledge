# Freeciv(nation) · colombian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/colombian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的colombian定义

## 正文
```ruleset
[nation_colombian]

name=_("Colombian")
plural=_("?plural:Colombians")
groups="Modern", "American"
legend=_("Colombia is a country in northern South America. The region was\
 an Amerindian cultural center in pre-European time. The Spanish began\
 settling Colombia's north coast around 1500. In 1819 the Republic of\
 Colombia gained independence.")

leaders = {
 "name",                                "sex"
 "G. Jiménez de Quesada",               "Male"
 "Francisco de Paula Santander",        "Male"
 "Simón Bolívar",                       "Male"
 "T. Cipriano de Mosquera",             "Male"
 "Rafael Núñez",                        "Male"
 "Jorge Eliécer Gaitán",                "Male"
 "Gustavo Rojas Pinilla",               "Male"
 "Alberto Lleras Camargo",              "Male"
 "Alfonso López Michelsen",             "Male"
 "Álvaro Uribe",                        "Male"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Communism",      _("Comandante %s"),   _("Comandanta %s")
 "Despotism",      _("General %s"),      _("?female:General %s")
 "Fundamentalism", _("Archbishop %s"),   _("Mother Superior %s")
 "Monarchy",       _("Viceroy %s"),      _("Vicereine %s")
}

flag="colombia"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Tairona"
civilwar_nations="Venezuelan", "Ecuadorian", "Panamanian"

cities =
 "Bogotá",
 "Medellín",
 "Santiago de Cali",
 "Barranquilla",
 "Cartagena de Indias",
 "Cúcuta",
 "Bucaramanga",
 "Manizales",
 "Ibagué",
 "Pereira",
 "Arauca",
 "Armenia",
 "Barrancabermeja",
 "Buenaventura",
 "Florencia",
 "Leticia",
 "Mocoa",
 "Montería",
 "Neiva",
 "Palmira",
 "Pasto",
 "Popayán",
 "Quibdó",
 "Riohacha",
 "San José del Guaviare",
 "Santa Marta",
 "Sincelejo",
 "Tunja",
 "Valledupar",
 "Villavicencio",
 "Yopal",
 "Girardot",
 "Maicao",
 "Mompós",
 "San Vicente de Caguán"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
