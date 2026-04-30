# Freeciv(nation) · saxon

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/saxon.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的saxon定义

## 正文
```ruleset
[nation_saxon]

name=_("Saxon")
plural=_("?plural:Saxons")
groups="Medieval", "Early Modern", "European"
legend=_("The Electorate of Saxony was an independent hereditary electorate\
 of the Holy Roman Empire from 1356-1806.")

leaders = {
 "name",                        "sex"
 "Rudolf I",                    "Male"
 "Johann Georg I",		"Male"
 "Friedrich August I",          "Male"
 "Friedrich August II",         "Male"
 "Friedrich August III",        "Male"
}

ruler_titles = {
 "government",       "male_title",       "female_title"
 "Democracy", _("Minister-President %s"), _("?female:Minister-President %s")
 "Despotism",        _("Duke %s"),       _("Duchess %s")
 "Fundamentalism",   _("Bishop %s"),     _("?female:Bishop %s")
}

flag="saxony"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "sorbian", "hanoverian", "thuringian", "anhaltian"

cities =
; Electoral/Royal Saxony
  "Wittenberg",
  "Dresden",
  "Leipzig",
  "Chemnitz",
  "Bautzen",
  "Görlitz",
  "Löbau",
  "Zittau",
  "Merseburg",
  "Königstein",
  "Pirna",
  "Johanngeorgenstadt",
  "Zwickau",
  "Freiberg",
  "Grimma",
  "Oschatz",
  "Meißen",
  "Naumburg",
  "Torgau",
  "Lübben",
  "Guben",
  "Eilenburg",
  "Düben",
  "Schwarzenberg",
  "Marienberg",
  "Kamenz",
  "Annaberg",
  "Flöha",
  "Dippoldiswalde",
  "Großenhain",
  "Borna",
  "Döbeln",
  "Rochlitz",
  "Auerbach",
  "Oelsnitz",

; Prussian Province of Saxony
  "Magdeburg",
  "Halle/Saale",
  "Mühlhausen",
  "Halberstadt",
  "Stendal",
  "Nordhausen",
  "Quedlinburg",
  "Bad Langensalza",

; Saxon duchies
  "Weimar",
  "Gotha",
  "Coburg",
  "Altenburg",
  "Meinigen",
  "Hildburghausen",
  "Saalfeld",
  "Lauenburg/Elbe",

; Lower Saxony
  "Hannover",
  "Oldenburg",
  "Osnabrück",
  "Braunschweig",
  "Lüneburg",
  "Göttingen",
  "Salzgitter"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
