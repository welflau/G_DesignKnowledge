# Freeciv(nation) · bulgarian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/bulgarian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的bulgarian定义

## 正文
```ruleset
[nation_bulgarian]

name=_("Bulgarian")
plural=_("?plural:Bulgarians")
groups="Modern", "Medieval", "European"
legend=_("Bulgar leader Khan Asparukh led his people into the northern\
 Balkans, and founded Bulgaria in 681. This was the first Slavic\
 nation-state in history.")

leaders = {
 "name",                        "sex"
 "Asparukh",                    "Male"
 "Omurtag",                     "Male"
 "Kardam",                      "Male"
 "Krum",                        "Male"
 "Boris",                       "Male"
 "Simeon",                      "Male"
 "Samuil",                      "Male"
 "Petar",                       "Male"
 "Assen",                       "Male"
 "Kaloyan",                     "Male"
 "Ivan-Assen",                  "Male"
 "Ivaylo",                      "Male"
 "Ivan Shishman",               "Male"
 "Alexander I Battemberg",      "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Monarchy",        _("Tsar %s"),         _("Tsaritsa %s")
 "Fundamentalism",  _("Patriarch %s"),    _("Matriarch %s")
}

flag="bulgaria"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="romanian", "macedonian"

cities =
 "Sofia",
 "Plovdiv",
 "Varna",
 "Burgas",
 "Pleven",
 "Stara Zagora",
 "Rousse",
 "Montana",
 "Kjustendil",
 "Pazardzhik",
 "Razgrad",
 "Haskovo",
 "Smolian",
 "Kyrzdhali",
 "Dobrich",
 "Krichim",
 "Oriahovo",
 "Veliko Tyrnovo",
 "Vraca",
 "Lovech",
 "Biala",
 "Elena",
 "Dupnica",
 "Bansko",
 "Samokov",
 "Kostenec",
 "Asenovgrad",
 "Vidin",
 "Lom",
 "Karlovo",
 "Kazanlyk",
 "Zlatica",
 "Pirdop",
 "Elin Pelin",
 "Bankya",
 "Krumovgrad",
 "Pernik",
 "Tryn",
 "Breznik",
 "Zemen",
 "Petrich",
 "Stanke Dimitrov",
 "Chepelare",
 "Dimitrovgrad",
 "Slivnica",
 "Dragoman",
 "Sozopol",
 "Ahtopol",
 "Pomorie",
 "Primorsko",
 "Kavarna",
 "Aitos",
 "Karnobat",
 "Shumen",
 "Yambol",
 "Kotel",
 "Ugarchin",
 "Svoge",
 "Levski",
 "Svilengrad",
 "Malko Tyrnovo",
 "Devnya",
 "Godech",
 "Teteven",
 "Troyan",
 "Yablanitza",
 "Botevgrad",
 "Kula",
 "Nikopol",
 "Silistra",
 "Kostinbrod",
 "Koprivshtica",
 "Panagyurishte",
 "Peryshtica",
 "Ihtiman"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
