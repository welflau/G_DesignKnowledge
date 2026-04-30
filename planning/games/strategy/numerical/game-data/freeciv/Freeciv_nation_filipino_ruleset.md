# Freeciv(nation) · filipino

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/filipino.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的filipino定义

## 正文
```ruleset
[nation_filipino]

name=_("Filipino")
plural=_("?plural:Filipinos")
groups="Modern", "Asian"
conflicts_with="czech"	; Similar flags
legend=_("After centuries of Spanish rule, the Philippines were ceded to\
 the Americans in 1898. They attained home rule in 1935 and independence in\
 1946.")

leaders = {
 "name",                "sex"
 "Ramon Magsaysay",     "Male"
 "Jose Rizal",          "Male"
 "Luis Taruc",          "Male"
 "Sergio Osmeña",       "Male"
 "Ferdinand Marcos",    "Male"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Fundamentalism",  _("Cardinal %s"),       _("Mother Superior %s")
 "Republic",        _("Governor %s"),       _("?female:Governor %s")
}
flag="philippines"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="japanese", "malaysian"

cities =
  "Manila", "Cebu", "Makati", "Quezon", "Pasig", "Angeles", "Davao",
  "San Fernando", "Puerto Princesa", "Cagayan de Oro", "Zamboanga",
  "Bacolod", "Butuan", "Puerto Galera", "Olongapo", "Los Banos", "Lipa",
  "Batangas", "Naga", "Bauang", "Agoo", "San Pablo", "Calamba",
  "Iloilo", "Lucena", "Cabanatuan"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
