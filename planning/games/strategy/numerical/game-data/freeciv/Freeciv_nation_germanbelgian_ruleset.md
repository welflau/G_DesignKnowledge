# Freeciv(nation) · germanbelgian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/germanbelgian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的germanbelgian定义

## 正文
```ruleset
[nation_germanbelgian]

name=_("German Belgian")
plural=_("?plural:German Belgians")
groups= "European"
legend=_("The German-speaking Community is one of the three federal\
 communities of Belgium, part of the Walloon Region in the extreme east\
 of the country. The area was annexed by Belgium after the First World\
 War to compensate the country for the German occupation during that war.\
 With about 75,000 inhabitants the German-speaking Community comprises\
 less than one percent of Belgium's population. Long neglected, the\
 German-speaking Belgians now enjoy the same rights as their Flemish and\
 French-speaking compatriots. As a result, they are often dubbed 'the best\
 protected minority of Europe' and 'the last true Belgians'.")

leaders = {
 "name",                   "sex"
 "Bernhard von Scheibler", "Male"
 "Hugo Zimmermann",        "Male"
 "Leo Trouet",             "Male"
 "Karl-Heinz Lambertz",    "Male"
}

ruler_titles = {
 "government",     "male_title",                "female_title"
 "Democracy",      _("Minister-President %s"),  _("?female:Minister-President %s")
 "Fundamentalism", _("Abbot %s"),               _("Mother Superior %s")
}

flag="dgb"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "walloon", "luxembourgish", "rhenish"

cities =
 "Eupen",
 "Sankt Vith",
 "Kelmis",
 "Raeren",
 "Bütgenbach",
 "Büllingen",
 "Amel",
 "Lontzen",
 "Burg-Reuland",
 "Kettenis",
 "Recht",
 "Elsenborn",
 "Hauset",
 "Schönberg",
 "Meyerode",
 "Manderfeld",
 "Crombach",
 "Heppenbach",
 "Lommersweiler",
 "Neu-Moresnet",
 "Thommen",
 "Reuland",
 "Eynatten",
 "Walhorn",
 "Hergenrath",
 "Herbesthal",
 "Mürringen",
 "Neudorf",
 "Astenet",
 "Oberhausen",
 "Born",
 "Iveldingen",
 "Medell",
 "Wiesenbach",
 "Losheimergraben",
 "Busch",
 "Wereth",
 "Merols",
 "Ouren",
 "Steffeshausen",
 "Schlierbach",
 "Wallerode",
 "Hünningen",
 "Schoppen",
 "Deidenberg",
 "Krewinkel",
 "Möderscheid",
 "Rocherath",
 "Krinkelt",
 "Berg",
 "Hünningen",

 "Malmedy",
 "Weismes",
 "Bellevaux-Ligneuville",
 "Bévercé",
 "Robertville",
 "Faymonville"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
