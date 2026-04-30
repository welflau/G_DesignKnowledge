# Freeciv(nation) · liechtensteiner

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/liechtensteiner.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的liechtensteiner定义

## 正文
```ruleset
[nation_liechtensteiner]

name=_("Liechtensteiner")
plural=_("?plural:Liechtensteiners")
groups="Early Modern", "Modern", "European"
legend=_("The Principality of Liechtenstein is a tiny, doubly landlocked\
 alpine country in Western Europe, bordered by Switzerland to its west\
 and by Austria to its east. The Principality was formed by the merger\
 of Vaduz and Schellenberg in 1719.")

leaders = {
 "name",                "sex"
 "Karl I",              "Male"
 "Karl Eusebius",       "Male"
 "Hans-Adam I",         "Male"
 "Josef Wenzel",        "Male"
 "Anton Florian",       "Male"
 "Josef Johann Adam",   "Male"
 "Johann Nepomuk Karl", "Male"
 "Franz Josef I",       "Male"
 "Alois I",             "Male"
 "Johann I",            "Male"
 "Alois II",            "Male"
 "Johann II",           "Male"
 "Franz Josef II",      "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Despotism",       _("Prince %s"),          _("Princess %s")
 "Monarchy",        _("Grand Prince %s"),    _("Grand Princess %s")
 "Fundamentalism",  _("Bishop %s"),          _("Mother Superior %s")
}

flag="liechtenstein"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""
conflicts_with = "haitian" ;similar flag
civilwar_nations = "austrian", "swiss"

cities =
 "Vaduz (plains)",
 "Schellenberg (hills)",
 "Schaan (plains)",
 "Triesenberg (mountains)",
 "Triesen (plains)",
 "Ruggell (hills)",
 "Planken",
 "Balzers (plains)",
 "Mauren (plains)",
 "Eschen (plains)",
 "Gamprin (hills)",
 "Bendern",
 "Nendeln",
 "Schaanwald",
 "Masescha",
 "Silum",
 "Mäls",
 "Gaflei",
 "Steg",
 "Malbun",
 "Ebenholz",
 "Hinterschellenberg",
 "Mühleholz",
 "Rotenboden",
 "Samina",
 "Sücka",
 "Wangerberg",
 "Sankt Luzisteig",
 "Gutenberg"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
