# Freeciv(nation) · sammarinese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/sammarinese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的sammarinese定义

## 正文
```ruleset
[nation_sammarinese]

name = _("Sammarinese")
plural = _("?plural:Sammarinese")
groups="European", "Modern", "Early Modern", "Medieval"
legend=_("San Marino is a tiny landlocked country on the Italian Peninsula.\
 It is the oldest independent republic in the world. According to legend,\
 it was founded by Saint Marinus in 301 CE.")

leaders = {
 "name",                        "sex"
 "Marino",                      "Male"
 "Gian Giacomo Angeli",         "Male"
 "Antonio Onofri",              "Male"
 "Domenico Maria Belzoppi",     "Male"
 "Domenico Fattori",            "Male"
 "Giuliano Gozi",               "Male"
 "Maria Lea Pedini-Angelini",   "Female"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Communism",       _("Chairman %s"),       _("Chairwoman %s")
 "Democracy",       _("Councillor %s"),     _("?female:Councillor %s")
 "Fundamentalism",  _("Abbot %s"),          _("Mother Superior %s")
 "Republic",        _("Captain-Regent %s"), _("?female:Captain-Regent %s")
}

flag = "san_marino"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Italian", "Papal"

cities =
 "San Marino",
 "Acquaviva",
 "Borgio Maggiore",
 "Chiesanuova",
 "Serravalle",
 "Domagnano",
 "Fiorentino",
 "Faetano",
 "Montegiardino",
 "Dogana",
 "Falciano",
 "Fiorina",
 "Piandivello",
 "Spaccio Giannoni",
 "Rovereta",
 "Ventoso",
 "Torraccia",
 "Cerbaiola",
 "Cailungo",
 "Montalbo",
 "Valgiurata",
 "Cà Chiavello",
 "Monte Pulito",
 "Cà Ragni",
 "Corianino",
 "Molarini",
 "Ponte Mellini",
 "San Giovanni sotto le Penne",
 "Crociale",
 "Poggio Chiesanuova",
 "Canepa",
 "Castellaro",
 "Capanne",
 "Poggio Casalino",
 "Valdragone",
 "Santa Mustiola",
 "Cà Rigo",
 "Confine",
 "Pianacci",
 "Gualdicciolo",
 "Casole",
 "Calligaria",
 "Cà Giannino",
 "Cinque Vie",
 "Cà Berlone",
 "Murata",
 "Caladino",
 "Cà Melone",
 "Galavotto",
 "Lesignano",
 "Teglio",
 "La Serra"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
