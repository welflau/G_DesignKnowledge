# Freeciv(nation) · southafrican

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/southafrican.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的southafrican定义

## 正文
```ruleset
[nation_southafrican]

name=_("South African")
plural=_("?plural:South Africans")
groups="Modern", "African"
legend=_("Dutch settlers began colonizing southern Africa in the 17th\
 century. After many wars between primarily Boers (descendants of Dutch\
 settlers), British forces and Zulus, the Union of South Africa was created\
 in 1910. The South African government became notorious for its\
 \"apartheid\" policy of legal inequality based on the color of a citizen's\
 skin. Following the adoption of the country's first non-racist constitution\
 in 1994, long-time political prisoner Nelson Mandela became the\
 first truly democratically elected president of South Africa.")

leaders = {
 "name",                "sex"
 "Nelson Mandela",      "Male"
 "P.W. Botha",          "Male"
 "J.C. Smuts",          "Male"
 "H.F. Verwoerd",       "Male"
}
ruler_titles = {
 "government",     "male_title",       "female_title"
 "Fundamentalism", _("Archbishop %s"), _("?female:Archbishop %s")
} 
flag="south_africa"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="boer", "zulu", "xhosa", "venda", "sotho", "tswana"
civilwar_nations="boer", "zulu", "xhosa", "venda", "namibian", "sotho", "tswana"

; The three capitals at top and the rest in order of population as of 2005
; http://de.wikipedia.org/wiki/Liste_der_Städte_in_Südafrika
cities =
 "Kaapstad",
 "Pretoria",
 "Bloemfontein",
 "Johannesburg",
 "Durban",
 "Soweto",
 "Port Elizabeth (ocean)",
 "Pietermaritzburg",
 "Benoni",
 "Tembisa",
 "Vereeniging",
 "Boksburg",
 "Welkom",
 "East London",
 "Newcastle",
 "Krugersdorp",
 "Botshabelo",
 "Brakpan",
 "Witbank",
 "Richards Bay (ocean)",
 "Vanderbijlpark",
 "Centurion",
 "Uitenhage",
 "Alberton",
 "Paarl",
 "Springs",
 "Somerset West",
 "Carltonville",
 "Klerksdorp",
 "George",
 "Midrand",
 "Westonaria",
 "Middelburg",
 "Vryheid",
 "Orkney",
 "Kimberley",
 "Embalenhle",
 "Nigel",
 "Epumalanga",
 "Bisho",
 "Randfontein",
 "Worcester",
 "Rustenburg",
 "Polokwane",
 "Potchefstroom",
 "Virginia",
 "Brits",
 "Emnambithi",
 "Nelspruit",
 "Phalaborwa",
 "Queenstown",
 "Kroonstad",
 "Bethal",
 "Potgietersrus"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
