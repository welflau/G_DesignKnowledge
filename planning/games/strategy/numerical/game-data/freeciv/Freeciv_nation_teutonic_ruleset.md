# Freeciv(nation) · teutonic

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/teutonic.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的teutonic定义

## 正文
```ruleset
[nation_teutonic]

name=_("Teutonic")
plural=_("?plural:Teutonic Order")
groups="European", "Medieval"
legend=_("The Teutonic Order led a series of crusades against pagan Balts\
 during the High Middle Ages. In 1224 it founded the 'Ordenstaat' or State\
 of the Order, which remained a powerful country for three centuries. The\
 State was secularized and replaced by the Duchy of Prussia in the 16th\
 century.")

leaders = {
 "name",                                "sex"
 "Hermann von Salza",                   "Male"
 "Anno von Sangershausen",              "Male"
 "Hartmann von Heldrungen",             "Male"
 "Karl von Trier",                      "Male"
 "Winrich von Kniprode",                "Male"
 "Konrad von Jungingen",                "Male"
 "Paul von Rusdorf",                    "Male"
 "Ludwig von Erlichshausen",            "Male"
 "Martin Truchseß von Wetzhausen",      "Male"
 "Friedrich von Sachsen",               "Male"
 "Albrecht von Brandenburg-Ansbach",    "Male"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Fundamentalism", _("Archbishop %s"),   _("Mother Superior %s")
 "Despotism",      _("Master %s"),       _("Mistress %s")
 "Monarchy",       _("Grand Master %s"), _("Grand Mistress %s")
 "Democracy",      _("Chancellor %s"),   _("?female:Chancellor %s")
}

flag="teutonic_order"
flag_alt = "hre"
style = "European"

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "prussian", "german"
civilwar_nations = "estonian", "latvian", "prussian", "samogitian", "curonian"

cities =
 "Marienburg",
 "Königsberg",
 "Elbing",
 "Wenden",
 "Insterburg",
 "Allenburg",
 "Memel",
 "Riga",
 "Reval",
 "Bartenstein",
 "Heilsberg",
 "Osterode",
 "Neidenburg",
 "Straßburg",
 "Christburg",
 "Tapiau",
 "Thorn",
 "Braunsberg",
 "Kulm",
 "Windau",
 "Goldingen",
 "Kokenhausen",
 "Groß Roop",
 "Lemsal",
 "Wolmar",
 "Pernau",
 "Fellin",
 "Dorpat",
 "Wesenberg",
 "Narwa",
 "Danzig",
 "Tuchel",
 "Schlochau",
 "Hammerstein",
 "Dramburg",
 "Arnswalde",
 "Neu-Landsberg",
 "Dobrin",
 "Balga",
 "Ragnit",
 "Angerburg",
 "Rhein",
 "Ortelsburg",
 "Rehden",
 "Grobin",
 "Mitau",
 "Kreutzburg",
 "Dünaburg",
 "Rositten",
 "Ludsen",
 "Arensburg"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
