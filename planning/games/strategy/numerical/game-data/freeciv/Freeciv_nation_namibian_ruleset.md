# Freeciv(nation) · namibian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/namibian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的namibian定义

## 正文
```ruleset
[nation_namibian]

name=_("Namibian")
plural=_("?plural:Namibians")
groups="African", "Modern"

legend=_("Although European Powers long neglected the desertic\
 African Southwest, the German Empire established a colony\
 there in the late nineteenth century. After losing World War I,\
 the territory became a mandate under the responsibility of the\
 Union of South Africa. It finally became independent in 1990,\
 under the name of Namibia.")

leaders = {
 "name",                "sex"
 "Sam Nujoma",          "Male"
 "Samuel Maharero",     "Male"
 "Jakobus Morenga",     "Male"
 "Hendrik Witbooi",     "Male"
}

ruler_titles = {
 "government",  "male_title",         "female_title"
 "Republic",    _("Spokesman %s"),    _("Spokeswoman %s")
}

flag = "namibia"
flag_alt = "rwanda"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="south african", "khoisan", "boer"

; Based on http://de.wikipedia.org/wiki/Liste_der_Städte_in_Namibia

cities =

"Windhoek",
"Rundu",
"Walvis Bay (ocean)",
"Oshakati",
"Swakopmund",
"Katima Mulilo",
"Grootfontein",
"Okahandja",
"Otjiwarongo",
"Rehoboth",
"Gobabis",
"Lüderitz",
"Keetmanshoop",
"Mariental",
"Khorixas",
"Omaruru",
"Tsumeb",
"Bethanien",
"Usakos",
"Ongwediva",
"Ondangwa",
"Oranjemund",
"Otjimbingwe",
"Karibib",
"Warmbad",
"Outjo",
"Karasburg",
"Okakarara",
"Opuwo",
"Otavi",
"Arandis",
"Hentiesbaai (ocean)",
"Aranos",
"Eenhana",
"Outapi",
"Ongandjera",
"Okombahe",
"Oshikango",
"Maltahöhe"
 

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
