# Freeciv(nation) · lippe

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/lippe.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的lippe定义

## 正文
```ruleset
[nation_lippian]

name=_("Lippian")
plural=_("?plural:Lippians")
groups="European", "Medieval", "Early Modern"
legend=_("Lippe was a historical state in Germany. It was located between\
 the Weser River and the southeast part of the Teutoburg forest.")
leaders = {
 "name",                "sex"
 "Bernhard",            "Male"
 "Simon V",             "Male"
 "Bernhard VIII",       "Male"
 "Simon Ludwig",        "Male"
 "Johannes Bernhard",   "Male"
 "Friedrich Adolf",   	 "Male"
 "Simon Augustus",      "Male"
 "Pauline",             "Female"
 "Adolf I Georg",       "Male"
 "Woldemar",            "Male"
}

flag="lippe"
flag_alt = "-"
style = "European"

ruler_titles = { "government",      "male_title",      "female_title"
                 "Despotism",       _("Prince %s"),    _("Princess %s")
                 "Democracy", _("Minister-President %s"), _("?female:Minister-President %s")
                 "Fundamentalism",  _("Bishop %s"),    _("?female:Bishop %s")
               }

init_techs=""
init_buildings=""
init_units=""

conflicts_with="german"
civilwar_nations = "westphalian", "hanoverian", "saxon"

cities =
;Lippe-Detmold
 "Detmold",
 "Oerlinghausen",
 "Lügde",
 "Blomberg",
 "Bad Salzuflen",
 "Lemgo",
 "Barntrup",
 "Lage",
 "Horn",
 "Schwalenberg",
 "Augustdorf",
 "Extertal",	
 "Dörentrup",
 "Kalletal",
 "Schlangen",
 "Leopoldshöhe",
 "Alverdissen",
 "Schieder",
 "Bad Meinberg",
 "Varenholz",
 "Hohenthausen",
 "Grevenhagen",
 "Lipperode",
 "Biesterfeld",

;Schaumburg-Lippe
 "Bückeburg",
 "Stadthagen",
 "Hagenburg"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
