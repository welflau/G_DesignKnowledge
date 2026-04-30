# Freeciv(nation) · bissauguinean

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/bissauguinean.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的bissauguinean定义

## 正文
```ruleset
[nation_bissauguinean]

name = _("Bissau-Guinean")
plural = _("?plural:Bissau-Guineans")
groups="African", "Modern"
legend=_("Guinea-Bissau is a country in West Africa. Formerly known as\
 Portuguese Guinea, it declared independence in 1973.")

leaders = {
 "name",                 "sex"
 "Nuno Tristão",         "Male"
 "Amílcar Cabral",       "Male"
 "Luis Cabral",          "Male"
 "Carmen Pereira",       "Female"
 "João Bernardo Vieira", "Male"
 "Ansumane Mané",        "Male"
 "Kumba Yalá",           "Male"
}

ruler_titles = {
 "government",      "male_title",          "female_title"
 "Despotism",       _("Captain-Major %s"), _("?female:Captain-Major %s")
 "Fundamentalism",  _("Padre %s"),         _("Madre %s")
}

flag = "guinea-bissau"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="guinean", "cape verdean"

cities =
 "Bissau",
 "Bolama",
 "Cacheu",
 "Gabú",
 "Bafatá",
 "Catió",
 "Buba",
 "Farim",
 "Quinhámel",
 "Canghungo",
 "Bissorã",
 "Mansôa",
 "Safim",
 "Quebo",
 "Ingoré",
 "Bula",
 "São Domingos",
 "Bubaque",
 "Bambadinca",
 "Caboxanque",
 "Piche",
 "Paunca",
 "Contuboel",
 "Pelundo",
 "Mansabá",
 "Nhacra",
 "Fasse",
 "Calequisse",
 "Olossato",
 "Cumeré",
 "Mato Farroba",
 "Fulacunda",
 "Contuba",
 "Prábis",
 "Cacine",
 "Jobicunda",
 "Empada",
 "Bigene",
 "Tite",
 "Canfate",
 "Utia"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
