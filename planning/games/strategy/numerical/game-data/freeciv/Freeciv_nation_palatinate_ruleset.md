# Freeciv(nation) · palatinate

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/palatinate.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的palatinate定义

## 正文
```ruleset
[nation_palatinate]

name=_("Palatinate")
plural=_("?plural:Palatinate Germans")
groups="Medieval", "Early Modern", "European"
legend=_("The Electoral Palatinate was one of the electorates of the Holy\
 Roman Empire, located on the banks of the Rhine. It had a volatile\
 political history, continuously splitting and reuniting. Elector\
 Frederick V's capture of the Bohemian throne sparked the Thirty Years\
 War in 1618, in which much of the area was devastated. The Palatinate\
 was united in a personal union with Bavaria in 1777. Currently it is\
 part of the German state of Rhineland-Palatinate, with smaller areas in\
 Baden-Wuerttemberg and Bavaria.")

leaders = {
 "name",			"sex"
 "Konrad der Staufer",		"male"
 "Ruprecht",			"male"
 "Ruprecht III",		"male"
 "Friedrich der Siegreiche",	"male"
 "Ottheinrich",			"male"
 "Friedrich V",			"male"
 "Elisabeth Charlotte",		"female"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Anarchy",         _("Usurper %s"),        _("?female:Usurper %s")
 "Despotism",       _("Count Palatine %s"), _("Countess Palatine %s")
 "Fundamentalism",  _("Prince-Bishop %s"),  _("Mother Superior %s")
 "Monarchy",        _("Elector %s"),        _("Electress %s")
 "Democracy",  _("Minister-President %s"), _("?female:Minister-President %s")
}

flag="palatinate"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "lorrain", "bavarian", "badian", "rhenish"

cities =
 "Heidelberg",
 "Mannheim",
 "Speyer",
 "Worms",
 "Neustadt an der Weinstraße",
 "Weinheim",
 "Schwetzingen",
 "Kaiserslautern",
 "Amberg",
 "Alzey",
 "Zweibrücken",
 "Ladenburg",
 "Mosbach",
 "Bad Kreuznach",
 "Frankenthal",
 "Landau in der Pfalz",
 "Pirmasens",
 "Bad Dürkheim",
 "Ludwigshafen",
 "Lindenfels",
 "Neumarkt",
 "Boxberg",
 "Kusel",
 "Germersheim",
 "Bretten",
 "Otzberg",
 "Umstadt",
 "Bacharach",
 "Neuburg an der Donau",
 "Neustadt am Kulm",
 "Birkenfeld",
 "Oppenheim",
 "Seltz",
 "Simmern",
 "Veldenz",
 "Sulzbach",
 "Bischweiler",
 "Lützelstein",
 "Rappoltstein",
 "Sponheim",
 "Eschenbach",
 "Sinsheim",
 "Traben-Trarbach",
 "Göllheim",
 "Kirchheimbolanden"



```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
