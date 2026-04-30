# Freeciv(nation) · briton

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/briton.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的briton定义

## 正文
```ruleset
[nation_briton]

name=_("Briton")
plural=_("?plural:Britons")
groups="Ancient", "European"
legend=_("The Britons were the inhabitants of most of Great Britain\
 during the Iron Age. They spoke Brythonic Celtic languages and are the\
 ancestors of the modern Welsh, Cornish and Breton people.")

leaders = {
 "name",                "sex"
 "Cunobelinos",         "Male"
 "Cassiwellaunos",      "Male"
 "Caratacos",           "Male"
 "Cartismandua",        "Female"
 "Boudica",             "Female"
}

ruler_titles = {
 "government",     "male_title",       "female_title"
 "Despotism",	   _("Chieftain %s"),  _("?female:Chieftain %s")
 "Fundamentalism", _("Druid %s"),      _("?female:Druid %s")
 "Monarchy",       _("High King %s"),  _("High Queen %s")
} 

flag="britannia"
flag_alt = "gaul"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="british", "welsh", "cornish", "breton"
civilwar_nations="welsh", "cornish", "breton", "galician"

cities =
 "Werulamion",
 "Camulodunon",
 "Londinion",
 "Eboracon",
 "Windolanda",
 "Dubris",
 "Bannawenta",
 "Callewa",
 "Dewa",
 "Corinion",
 "Durowernon",
 "Glewon",
 "Isca",
 "Lindo",
 "Abona",
 "Moridunon",
 "Isurion",
 "Windomora",
 "Petuaria",
 "Lactodoron",
 "Ratae",
 "Durnowaria",
 "Wenta",
 "Wenone",
 "Isannawantia",
 "Uriconon",
 "Nowiomagos",
 "Magiowinter",
 "Coria",
 "Luguwalion",
 "Senodunon",
 "Ledrid",
 "Dubras",
 "Ardotalia",
 "Concangis",
 "Durocornowion",
 "Letoceton",
 "Mamucion",
 "Lindinis",
 "Winowia",
 "Cructan",
 "Luention"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
