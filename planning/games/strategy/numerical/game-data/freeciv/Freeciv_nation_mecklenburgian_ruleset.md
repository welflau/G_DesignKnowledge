# Freeciv(nation) · mecklenburgian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/mecklenburgian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的mecklenburgian定义

## 正文
```ruleset
[nation_mecklenburgian]

name = _("Mecklenburgian")
plural = _("?plural:Mecklenburgians")
groups="European", "Medieval", "Early Modern"
legend=_("Mecklenburg was erected in the 12th century. Its ruling house,\
 the Obrodites, were of Slavic origin - unique amongst the German\
 states. The dynasty remained in power for eight centuries. The Duchy was\
 divided into Mecklenburg-Strelitz and Mecklenburg-Schwerin. In the 19th\
 century Mecklenburg got the reputation of being the most backward of the\
 German states; its feudal institutions were abolished only at the\
 downfall of the monarchy in 1918. Currently Mecklenburg forms the western\
 two thirds of the German state of Mecklenburg-Cispomerania.")
leaders = {
 "name",		"sex"
 "Niklot",		"male"
 "Pribislaw",		"male"
 "Heinrich Borwin II",	"male"
 "Albrecht II",		"male"
 "Heinrich dem Dicken",	"male"
 "Karl Leopold",	"male"
 "Christian Ludwig II",	"male"
 "Adolf Friedrich IV",	"male"
 "Friedrich Franz IV",	"male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Communism",       _("First Secretary %s"), _("?female:First Secretary %s")
 "Despotism",       _("Prince %s"),          _("Princess %s")
 "Fundamentalism",  _("Bishop %s"),          _("?female:Bishop %s")
 "Monarchy",        _("Grand Duke %s"),      _("Grand Duchess %s")
 "Democracy",  _("Minister-President %s"), _("?female:Minister-President %s")
}

flag = "mecklenburg"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="western pomeranian", "saxon", "brandenburgian"

cities =
 "Schwerin",
 "Strelitz",
 "Rostock",
 "Neubrandenburg",
 "Wismar",
 "Mecklenburg",
 "Neustrelitz",
 "Güstrow",
 "Ludwigslust",
 "Bad Doberan",
 "Waren",
 "Parchim",
 "Grevesmühlen",
 "Boizenburg/Elbe",
 "Ratzeburg",
 "Stargard",
 "Wenden",
 "Werle",
 "Richenberg",
 "Dömitz",
 "Malchin",
 "Schönberg",
 "Neuhaus",
 "Hagenow",
 "Plau am See",
 "Dambeck",
 "Gevezin",
 "Penzlin",
 "Buschhof",
 "Feldberg",
 "Rossow",
 "Friedland",
 "Fürstenberg",
 "Mirow",
 "Tornow",
 "Dodow",
 "Horst",
 "Brunow",
 "Walksfelde",
 "Mannhagen",
 "Gadebusch"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
