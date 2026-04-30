# Freeciv(nation) · schaumburglippe

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/schaumburglippe.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的schaumburglippe定义

## 正文
```ruleset
[nation_schaumburglippe]

name=_("Schaumburg-Lippe")
plural=_("?plural:Schaumburg-Lippians")
groups="European", "Medieval", "Early Modern"
legend=_("Schaumburg-Lippe was created as a county in 1647, became a principality in 1807,\
 a free state in 1918, and was until 1946 a small state in Germany.")
leaders = {
 "name",                			"sex"
 "Adolf II zu Schaumburg-Lippe.",            	"Male"
 "Philipp I zur Lippe-Alverdissen",             "Male"
 "Heinrich Lorenz",       			"Male"
 "Heinrich Drake",        			"Male"
}

flag="schaumburglippe"
flag_alt = "lusatia"  ; Similar colors
style = "European"

ruler_titles = { 
 "government",      "male_title",               "female_title"
 "Despotism",       _("Prince %s"),             _("Princess %s")
 "Democracy",       _("Minister-President %s"), _("?female:Minister-President %s")
 "Fundamentalism",  _("Bishop %s"),             _("?female:Bishop %s")
}

init_techs=""
init_buildings=""
init_units=""

conflicts_with="lippian"
civilwar_nations = "lippian", "westphalian", "hanoverian", "saxon"

cities =
 "Bückeburg",
 "Stadthagen", 
 "Bad Nenndorf",
 "Hagenburg",
 "Bad Eilsen",
 "Lindhorst",
 "Niedernwöhren", 
 "Nienstädt", 
 "Obernkirchen", 
 "Rinteln", 
 "Rodenberg",
 "Sachsenhagen",
 "Auetal"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
