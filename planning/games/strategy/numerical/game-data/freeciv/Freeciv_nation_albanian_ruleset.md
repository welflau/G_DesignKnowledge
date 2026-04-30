# Freeciv(nation) · albanian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/albanian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的albanian定义

## 正文
```ruleset
[nation_albanian]

name=_("Albanian")
plural=_("?plural:Albanians")
groups="Modern", "Medieval", "European"
legend=_("Inhabitants of the Balkan peninsula, the ethnic origins of the\
 Albanians are uncertain, though it has been suggested they descend from\
 the Illyrians of Classical Antiquity. Albania changed hands several\
 times during its history. It has been an independent state again since\
 1912. For much of the 20th century Albania was ruled by communist\
 dictator Envër Hoxha.")

leaders = {
 "name",                        "sex"
 "Dhimitër Progoni",            "Male"
 "Gjergj Kastrioti Skënderbeu", "Male"
 "Ismail Qemali",               "Male"
 "Esad Pashë Toptani",          "Male"
 "Ahmet Bej Zogu",              "Male"
 "Geraldina Zog",               "Female"
 "Envër Hoxha",                 "Male"
 "Ramiz Alia",                  "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Despotism",       _("Prince %s"),          _("Princess %s")
 "Communism",       _("First Secretary %s"), _("?female:First Secretary %s")
}

flag="albania"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

conflicts_with= "illyrian"
civilwar_nations = "hellenic", "kosovar", "italian"

cities =
 "Tiranë",
 "Durrës",
 "Vlorë",
 "Elbasan",
 "Shkodër",
 "Korçë",
 "Fier",
 "Gjirokastër",
 "Berat",
 "Lushnjë",
 "Sarandë",
 "Pogradec",
 "Laç",
 "Patos",
 "Krujë",
 "Kuçovë",
 "Kukës",
 "Lezhë",
 "Peshkopi",
 "Burrel",
 "Cërrik",
 "Çorovodë",
 "Shijak",
 "Librazhd",
 "Tepelenë",
 "Gramsh",
 "Poliçan",
 "Bulqizë",
 "Përmet",
 "Fushë-Krujë",
 "Kamëz",
 "Rrëshen",
 "Ballsh",
 "Mamurras",
 "Bajram Curri",
 "Ersekë",
 "Peqin",
 "Divjakë",
 "Selenicë",
 "Himarë",
 "Bilisht",
 "Roskovec",
 "Vorë",
 "Rrogozhinë",
 "Urë Vajgurore",
 "Pukë",
 "Koplik",
 "Mamaliaj",
 "Përrenjas",
 "Maliq",
 "Libobovë"




```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
