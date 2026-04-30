# Freeciv(nation) · badian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/badian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的badian定义

## 正文
```ruleset
[nation_badian]

name=_("Badian")
plural=_("?plural:Badians")
groups="Medieval", "Early Modern", "European"
legend=_("Baden was a country in Swabia, in southwestern Germany. After\
 World War II it was merged with Wuerttemberg and Hohenzollern to form\
 the land of Baden-Wuerttemberg.")

leaders = {
 "name",                "sex"
 "Berthold I",          "Male"
 "Hermann II",          "Male"
 "Karl Friedrich",      "Male"
 "Friedrich Hecker",    "Male"
 "Max von Baden",       "Male"
 "Adam Remmele",        "Male"
}

ruler_titles = {
 "government",      "male_title",       "female_title"
 "Democracy",       _("Minister-President %s"), _("?female:Minister-President %s")
 "Despotism",       _("Margrave %s"),   _("Margravine %s")
 "Fundamentalism",  _("Bishop %s"),     _("Mother Superior %s")
 "Monarchy",        _("Grand Duke %s"), _("Grand Duchess %s")
}

flag="baden"
flag_alt = "germany"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "wuerttembergian", "palatinate", "alsatian"

cities =
 "Baden",
 "Karlsruhe",
 "Mannheim",
 "Freiburg im Breisgau",
 "Konstanz",
 "Heidelberg",
 "Pforzheim",
 "Ettlingen",
 "Rastatt",
 "Lörrach",
 "Durlach",
 "Donaueschingen",
 "Kehl",
 "Yberg",
 "Gengenbach",
 "Hochberg",
 "Neckargemünd",
 "Dilsberg",
 "Villingen",
 "Waldshut",
 "Offenburg",
 "Mosbach",
 "Sinsheim",
 "Engen",
 "Meßkirch",
 "Pfullendorf",
 "Radolfzell",
 "Stokach",
 "Überlingen",
 "Triberg",
 "Bonndorf",
 "Jestetten",
 "Sankt Blasien",
 "Säckingen",
 "Breisach",
 "Emmendingen",
 "Ettenheim",
 "Kenzingen",
 "Neustadt",
 "Staufen",
 "Waldkirch",
 "Müllheim",
 "Schönau",
 "Schopfheim",
 "Lahr",
 "Oberkirch",
 "Wolfach",
 "Achern",
 "Bühl",
 "Gernsbach",
 "Bretten",
 "Bruchsal",
 "Schwetzingen",
 "Weinheim",
 "Eppingen",
 "Wiesloch",
 "Adelsheim",
 "Boxberg",
 "Buchen",
 "Eberbach",
 "Tauberbischofsheim",
 "Wertheim",
 "Walldürn"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
