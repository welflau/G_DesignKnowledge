# Freeciv(nation) · tairona

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/tairona.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的tairona定义

## 正文
```ruleset
[nation_tairona]

name=_("Tairona")
plural=_("?plural:Tairona")
groups="American"

legend=_("A Chibchan-speaking people related to the Kuna of Panama and the\
 Muisca of central Colombia, the Tairona inhabit the modern Magdalena and\
 La Guajira Departments of northern Colombia. Their city of Teyuna was\
 founded sometime around 500 BCE. The Tairona, living in a mountainous\
 area, built stone steps and terraces on steep hillsides in order to farm\
 the region. Though they fought against the Spanish for 75 years,\
 eventually they succumbed to the various pressures that all Native\
 American peoples were subject to during this period.")

leaders = {
 "name",                "sex"
 "Nabobá",              "Male"
 "Nugi Túxe",           "Male"
 "Hába Haxtoxé",        "Male"
 "Kunhwingumu",         "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Monarchy",        _("Paramount Chief %s"), _("?female:Paramount Chief %s")
}

flag         = "tairona"
flag_alt     = "-"
style        = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "inca", "kuna", "mwiska"

cities =
 "Teyuna",
 "Chengue",
 "Nehuange",
 "Gaira",
 "Cinto",
 "Buritaca",
 "Posiguieca",
 "Pongueyca",
 "Kogi",
 "Yechikin",
 "Busin",
 "Serankua",
 "Windiwameina",
 "Singunei",
 "Zigta",
 "Yeurwa",
 "Gumuke",
 "Yeiwin",
 "Seiarukwingumu",
 "Buyuaguenka",
 "Simonorwa",
 "Wirwa",
 "Yugaka",
 "Karwa",
 "Sogrome",
 "Donachwi",
 "Timaka",
 "Aruamake",
 "Seinimin",
 "Izrwa",
 "Bonda",
 "Concha",
 "Bunkunagega",
 "Mukuánauiaishi"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
