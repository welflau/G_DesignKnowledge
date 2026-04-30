# Freeciv(nation) · saarprotectorate

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/saarprotectorate.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的saarprotectorate定义

## 正文
```ruleset
[nation_saarprotectorate]

name=_("Saar Protectorate")
plural=_("?plural:Saarlanders")
groups="European"
legend=_("The Saar Protectorate was a short-lived protectorate (1947–56) \
partitioned from Germany after its defeat in World War II; \
it was administered by the French Fourth Republic. On rejoining West Germany \
in 1957, it became the smallest 'area state', the Saarland. It is named \
after the Saar River.")
;Legend from: https://en.wikipedia.org/wiki/Saar_Protectorate
leaders = {
 "name",                        "sex"
 "Johannes Hoffmann",           "Male"
 "Charles de Gaulle",           "Male"
 "Gilbert Grandval",     	"Male"
 "Hubert Ney",     		"Male"
 "Erich Honecker",           	"Male"
}

ruler_titles = {
 "government",      "male_title",              "female_title"
 "Despotism",       _("High Commissioner %s"), _("?female:High Commissioner %s")
 "Democracy",       _("Prime Minister %s"),    _("?female:Prime Minister %s")
 "Fundamentalism",  _("Archbishop %s"),        _("?female:Archbishop %s")
 "Communism",       _("First Secretary %s"),   _("?female:First Secretary %s")
 "Monarchy",        _("King %s"),              _("Queen %s")
}

flag="saarprotectorate"
flag_alt = "denmark"  ; Similar colors
style = "european"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="rhenish", "palatinate", "luxembourgish", "lorrain", "prussian"

cities =
 "Saarbrücken",
  "Neunkirchen", 
  "Homburg",
  "St. Ingbert",
  "Saarlouis",
  "Merzig", 
  "St. Wendel", 
  "Blieskastel", 
  "Dillingen/Saar", 
  "Lebach",
  "Püttlingen",
  "Bexbach", 
  "Sulzbach/Saar",
  "Wadern",
  "Ottweiler", 
  "Friedrichsthal", 
  "Heusweiler", 
  "Losheim am See",
  "Schiffweiler",
  "Tholey", 
  "Mettlach",
  "Überherrn",
  "Kleinbittersdorf", 
  "Wallerfangen", 
  "Nonnweiler"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
