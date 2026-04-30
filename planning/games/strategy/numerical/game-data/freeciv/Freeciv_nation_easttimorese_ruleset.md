# Freeciv(nation) · easttimorese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/easttimorese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的easttimorese定义

## 正文
```ruleset
[nation_easttimorese]

name=_("East Timorese")
plural=_("?plural:East Timorese")
groups="Oceanian", "Asian", "Modern"
legend=_("A former Portuguese colony, East Timor declared independence\
 in 1975 but was overrun by Indonesian forces shortly thereafter. East\
 Timor became the first newly sovereign state of the 21st century when\
 Indonesia relinquished control on May 20, 2002.")

leaders = {
 "name",                "sex"
 "José Ramos-Horta",    "Male"
 "Lúcia Lobato",        "Female"
 "Manuel Carrascalão",  "Male"
 "Nicolau Lobato",      "Male"
 "Baria Nahak",         "Male"
}

ruler_titles = {
 "government",     "male_title",    "female_title"
 "Fundamentalism", _("Bishop %s"),  _("Mother Superior %s")
}

flag="east_timor"
flag_alt="-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Indonesian", "Moluccan"

cities =
 "Dili",
 "Dare",
 "Lospalos",
 "Baucau",
 "Ermera",
 "Maliana",
 "Suai",
 "Bobonaro",
 "Viqueque",
 "Liquiçá",
 "Pante Macassar",
 "Metinaro",
 "Gleno",
 "Lolotoe",
 "Bazartete",
 "Lautém",
 "Ainaro",
 "Same",
 "Manatuto",
 "Aileu",
 "Quelicai",
 "Hatulia",
 "Bobonaro",
 "Maubisse",
 "Letefoho",
 "Uato-Lari",
 "Ossu",
 "Maubara",
 "Atsabe",
 "Laga",
 "Venilale",
 "Balibo",
 "Nitibe",
 "Hau-Builico",
 "Oesilo"




```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
