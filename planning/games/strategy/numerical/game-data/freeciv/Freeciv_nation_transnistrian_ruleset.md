# Freeciv(nation) · transnistrian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/transnistrian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的transnistrian定义

## 正文
```ruleset
[nation_transnistrian]

name=_("Transnistrian")
plural=_("?plural:Transnistrians")
groups="Modern", "European"
legend=_("Transnistria was added to the Moldavian SSR by Stalin, although\
 it was mostly inhabited by Russians and Ukrainians. After the collapse of\
 the Soviet Union Transnistria declared its independence from Moldova.\
 Although the country is de facto independent, it is not recognized by any\
 UN member. Power is still in the hands of the old communist elite.")
leaders = {
 "name",                        "sex"
 "Grigory Kotovsky",            "Male"
 "Igor Smirnov",                "Male"
 "Alena Arshinova",             "Female"
}
flag="transnistria"
flag_alt = "-"
style = "european"

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Communism",       _("First Secretary %s"), _("?female:First Secretary %s")
 "Despotism",       _("Commissar %s"),   _("?female:Commissar %s")
 "Fundamentalism",  _("Patriarch %s"),   _("Matriarch %s")
}

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "soviet", "ruthenian"
civilwar_nations = "moldovan", "russian"

cities = 
 "Tiraspol",
 "Rybnitsa",
 "Dubossary",
 "Slobodzeya",
 "Grigoriopol",
 "Dnestrovsk",
 "Novo-Tiraspolskiy",
 "Kamenka",
 "Mayak",
 "Krasnoye",
 "Bender",
 "Rashkovo",
 "Kolbasna",
 "Kolosovo",
 "Korotnoye",
 "Krasniy Oktyabr",
 "Vykhvatintsy",
 "Parkany",
 "Malayeshty",
 "Lenino",
 "Mokra",
 "Podoyma",
 "Popenki",
 "Voronkovo",
 "Stroentsy",
 "Tashlyk",
 "Ternovka",
 "Vadul-Turkuluy",
 "Valia-Adynka",
 "Sovyetskoye",
 "Katerinovska",
 "Novo-Komissarovska",
 "Dzerzhinskoye",
 "Frunze",
 "Severinovska",
 "Sloboda-Rashkov",
 "Vinogradnoye",
 "Vladimirobskiy"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
