# Freeciv(nation) · danish

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/danish.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的danish定义

## 正文
```ruleset
[nation_danish]

translation_domain="freeciv"

name=_("Danish")
plural=_("?plural:Danes")
groups="Modern", "Medieval", "Early Modern", "European", "Core"
legend=_("The founding of the Danish kingdom is generally assigned to the\
 reign of Harald Blåtand, who unified what is now Denmark between 958 CE\
 and 988 CE.")

; Leaders in chronological order according to:
; http://en.wikipedia.org/wiki/List_of_Danish_monarchs
leaders = {
 "name",                "sex"
 "Gorm den Gamle",      "Male"
 "Harald Blåtand",      "Male"
 "Svend Tveskæg",       "Male"
 "Knud den Store",      "Male"
 "Hardeknud",           "Male"
 "Svend Estridsen",     "Male"
 "Knud den Hellige",    "Male"
 "Valdemar den Store",  "Male"
 "Valdemar Sejr",       "Male"
 "Erik Glipping",       "Male"
 "Valdemar III",        "Male"
 "Valdemar Atterdag",   "Male"
 "Christian IV",        "Male"
 "Margrete I",          "Female"
}

ruler_titles = {
 "government",   "male_title",           "female_title"
 "Despotism",    _("Earl %s"),           _("?female:Earl %s")
}

flag="denmark"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "english", "icelandic", "norwegian", "schleswig-holsteinian",
 "scanian", "greenlander", "faroese"

cities =
 "København",
 "Aarhus",
 "Odense",
 "Aalborg",
 "Esbjerg",
 "Randers",
 "Frederikshavn",
 "Helsingør",
 "Roskilde",
 "Slagelse",
 "Sønderborg",
 "Åbenrå",
 "Haderslev",
 "Vejle",
 "Holstebro",
 "Hirtshals",
 "Tylstrup",
 "Skagen",
 "Hjørring",
 "Blokhus",
 "Nørresundby",
 "Hanstholm",
 "Thisted",
 "Løgstør",
 "Thyborøn",
 "Skive",
 "Hadsund",
 "Ålestrup",
 "Grenå",
 "Struer",
 "Herning",
 "Silkeborg",
 "Yding",
 "Skovhøj",
 "Give",
 "Tarm",
 "Varde",
 "Assens",
 "Nyborg",
 "Fåborg",
 "Korsør",
 "Næstved",
 "Vordingborg",
 "Nakskov",
 "Rødby",
 "Birkerød",
 "Nykøbing",
 "Rønne",
 "Allinge",
 "Neksø",
 "Fredericia",
 "Godthåb",
 "Julianehåb",
 "Daneborg"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
