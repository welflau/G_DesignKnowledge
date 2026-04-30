# Freeciv(nation) · hessedarmstadt

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/hessedarmstadt.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的hessedarmstadt定义

## 正文
```ruleset
[nation_hessedarmstadt]

name=_("Hesse-Darmstadt")
plural=_("?plural:Hesse-Darmstadter")
groups="European", "Early Modern"
legend=_("The Grand Duchy of Hesse existed from 1806 till 1918.\
 It emerged in 1806 from the Landgraviate of Hesse-Darmstadt.\
 When the monarchy was overthrown in 1918 it became the People's\
 State of Hesse.")

leaders = {
 "name",                                 "sex"
 "Georg I von Hessen-Darmstadt",         "Male"
 "Magdalena zur Lippe",                  "Female"
 "Ernst Ludwig",                         "Male"
 "Ludwig I",                             "Male"
 "Carl von Ewald",                       "Male"
 "Heinrich von Gagern",                  "Male"
 "Carl Grolman",                         "Male"
 "Christian Ewald",                      "Male"
 "Alice von Grossbritannien und Irland", "Female"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Democracy",       _("Chancellor %s"),      _("?female:Chancellor %s")
 "Fundamentalism",  _("Archbishop %s"),      _("?female:Archbishop %s")
 "Communism",       _("First Secretary %s"), _("?female:First Secretary %s")
 "Monarchy",        _("Grand Duke %s"),          _("Grand Duchess %s")
}

flag="hessedarmstadt"
flag_alt = "singapore"  ; Similar colors
style = "european"

init_techs=""
init_buildings=""
init_units=""

conflicts_with= "hessian"
civilwar_nations= "hanoverian", "badian", "palatinate", "rhenish", "lippian", "rhenish", "prussian", "lippian"

cities =
 "Darmstadt",
 "Offenbach", 
 "Mainz",
 "Worms",
 "Giessen",
 "Bensheim", 
 "Vilbel", 
 "Friedberg", 
 "Alsfeld", 
 "Biedenkopf",
 "Battenberg",
 "Vöhl", 
 "Wimpfen",
 "Lauterbach", 
 "Schlitz", 
 "Büdingen", 
 "Dieburg", 
 "Erbach",
 "Helmhof",
 "Heppenheim",
 "Neckarsteinach",
 "Schotten"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
