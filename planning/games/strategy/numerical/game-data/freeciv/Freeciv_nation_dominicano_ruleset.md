# Freeciv(nation) · dominicano

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/dominicano.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的dominicano定义

## 正文
```ruleset
[nation_dominicano]

name=_("Dominicano")
plural=_("?plural:Dominicanos")
groups="Modern", "American"
legend=_("The Dominican Republic is located on the eastern two thirds of\
 the Caribbean island of Hispaniola. Its capital - Santo Domingo - became\
 the first permanent European settlement in the Americas when it was\
 founded by Bartholomew Columbus in 1498.")

leaders = {
 "name",                        "sex"
 "Cristobal Colón",             "Male"
 "Juan Pablo Duarte",           "Male"
 "Pedro Santana",               "Male"
 "Buenaventura Báez",           "Male"
 "Ulises Heureaux",             "Male"
 "Horacio Vásquez",             "Male"
 "Rafael Leónidas Trujillo",    "Male"
 "Juan Bosch",                  "Male"
 "Joaquín Balaguer",            "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("General %s"),      _("?female:General %s")
 "Fundamentalism",  _("Archbishop %s"),   _("Mother Superior %s")
 "Monarchy",        _("Viceroy %s"),      _("Vicereine %s")
}

flag="dominican_republic"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Haitian", "Puerto Rican"

cities =
 "Santo Domingo",
 "Santiago de los Caballeros",
 "Puerto Plata",
 "San Pedro de Macorís",
 "La Romana",
 "Los Alcarrizos",
 "San Francisco de Macorís",
 "San Cristóbal",
 "Higüey",
 "La Vega",
 "Barahona",
 "Bonao",
 "San Juan de la Maguana",
 "Baní",
 "Haina",
 "Moca",
 "Azua",
 "Mao",
 "Boca Chica",
 "Cotuí",
 "Esperanza",
 "Villa Altagracia",
 "Hato Mayor del Rey",
 "Nagua",
 "Bajos de Haina",
 "Villa Bisonó",
 "Jarabacoa",
 "Constanza",
 "Consuelo",
 "Pedro Brand",
 "El Seibo",
 "Tamboril",
 "Bayaguana",
 "San Matas de Farfán",
 "San José de Ocoa",
 "Quisqueya",
 "Monte Cristi",
 "Neyba",
 "Sabana Grande de Boyá",
 "La Victoria",
 "Dajabón",
 "Sabaneta",
 "Monte Plata",
 "Maimón",
 "Duvergé",
 "Cambita Garabitos",
 "Sabana de la Mar (ocean)",
 "Guerra",
 "Comendador",
 "San Gregorio de Nigua",
 "Samaná",
 "Cabral"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
