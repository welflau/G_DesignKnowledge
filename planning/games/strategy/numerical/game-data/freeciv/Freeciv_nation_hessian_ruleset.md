# Freeciv(nation) · hessian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/hessian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的hessian定义

## 正文
```ruleset
[nation_hessian]

name=_("Hessian")
plural=_("?plural:Hessians")
groups="European", "Early Modern", "Medieval"
legend=_("Hesse became a landgraviate of the Holy Roman Empire in the\
 13th century. In the 16th century it splintered into a a number of\
 smaller territories. Many Hessians fought in the American Revolution as\
 mercenaries on both sides. Currently Hesse is one of the states of the\
 Federal Republic of Germany.")

leaders = {
 "name",                        "sex"
 "Heinrich das Kind",           "Male"
 "Otto das Kind",               "Male"
 "Heinrich II der Eiserne",     "Male"
 "Ludwig der Friedfertige",     "Male"
 "Ulrich von Hutten",           "Male"
 "Philipp I der Großmütige",    "Male"
 "Wilhelm IV der Weise",        "Male"
 "Friedrich von Schweden",      "Male"
 "Ludwig X",                    "Male"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Despotism",       _("Landgrave %s"),   _("Landgravine %s")
 "Fundamentalism",  _("Bishop %s"),      _("?female:Bishop %s")
 "Monarchy",        _("Elector %s"),     _("Electress %s")
 "Democracy", _("Minister-President %s"), _("?female:Minister-President %s")
}

flag="hesse"
flag_alt = "germany"
style = "european"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="hanoverian", "badian", "palatinate", "rhenish"

cities =
 "Kassel",
 "Marburg",
 "Darmstadt",
 "Wiesbaden",
 "Homburg",
 "Frankfurt am Main",
 "Nassau",
 "Offenbach am Main",
 "Hanau",
 "Mainz",
 "Weilburg",
 "Gießen",
 "Fulda",
 "Rüsselsheim",
 "Wetzlar",
 "Rodgau",
 "Oberursel",
 "Worms",
 "Dreieich",
 "Bensheim",
 "Hofheim",
 "Arolsen",
 "Maintal",
 "Langen",
 "Neu-Isenburg",
 "Bingen",
 "Mörfelden-Walldorf",
 "Limburg",
 "Dietzenbach",
 "Viernheim",
 "Nauheim",
 "Vilbel",
 "Lampertheim",
 "Hersfeld",
 "Alzey",
 "Taunusstein",
 "Friedberg",
 "Baunatal",
 "Kelkheim",
 "Rödermark",
 "Griesheim",
 "Hattersheim",
 "Heppenheim",
 "Nieder-Olm",
 "Butzbach",
 "Pfungstadt",
 "Korbach",
 "Friedrichsdorf",
 "Dillenburg",
 "Weiterstadt",
 "Obertshausen",
 "Groß-Gerau",
 "Idstein",
 "Ingelheim",
 "Karben",
 "Stadtallendorf",
 "Gelnhausen",
 "Groß-Umstadt",
 "Rheinfels"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
