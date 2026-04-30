# Freeciv(nation) · montenegrin

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/montenegrin.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的montenegrin定义

## 正文
```ruleset
[nation_montenegrin]

name=_("Montenegrin")
plural=_("?plural:Montenegrins")
groups="Modern", "Early Modern", "Medieval", "European"
legend=_("Montenegro is a small country on the Balkans, the last to be\
 conquered by the Ottomans and the first to become independent again.\
 Part of Yugoslavia in the 20th century, it dissolved its union\
 with Serbia in 2006.")

leaders = {
 "name",                                "sex"
 "Mihailo I",                           "Male"
 "Balša I ",                            "Male"
 "Đurađ V Crnojević",                   "Male"
 "Petar II Petrović-Njegoš",            "Male"
 "Danilo I Petrović-Njegoš",            "Male"
 "Nikola I Mirkov Petrović-Njegoš",     "Male"
 "Jelena Petrović-Njegoš",              "Female"
 "Krsto Zrnov Popović",                 "Male"
 "Veljko Milatović",                    "Male"
 "Milo Đukanović",                      "Male"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Despotism",       _("Prince %s"),         _("Princess %s")
 "Fundamentalism",  _("Prince-Bishop %s"),  _("Princess-Bishop %s")
 "Monarchy",        _("Grand Prince %s"),   _("Grand Princess %s")
}

flag="montenegro"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "serbian", "bosnian-herzegovinian", "albanian", "italian"

cities =
 "Podgorica",
 "Nikšić",
 "Kotor (ocean)",
 "Pljevlja",
 "Bijelo Polje",
 "Bar",
 "Cetinje",
 "Herceg Novi",
 "Budva",
 "Berane",
 "Ulcinj",
 "Tivat",
 "Rožaje",
 "Dobrota",
 "Danilovgrad",
 "Tuzi",
 "Bijela",
 "Mojkovac",
 "Škaljari",
 "Igalo",
 "Plav",
 "Burtaiši",
 "Ibarac",
 "Kolašin",
 "Golubovci",
 "Šušanj",
 "Resnik",
 "Nedakusi",
 "Sutomore",
 "Risan",
 "Ozrinići",
 "Mojanovići",
 "Baošići",
 "Potkrajci",
 "Žabljak",
 "Pešca",
 "Budimlja",
 "Mrčevac",
 "Stari Bar",
 "Donje Luge",
 "Polje",
 "Spuž",
 "Zelenika",
 "Beran Zelo",
 "Rastovac"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
