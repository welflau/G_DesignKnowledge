# Freeciv(nation) · czech

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/czech.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的czech定义

## 正文
```ruleset
[nation_czech]

name = _("Czech")
plural = _("?plural:Czechs")
groups="Modern", "Medieval", "European"
legend=_("Today's Czech Republic was until 1993 part of Czechoslovakia,\
 which had been until 1918 part of the Austro-Hungarian Empire.")

leaders = {
 "name",                "sex"
 "Jan Lucemburský",     "Male"
 "Otakar II",           "Male"
 "Karel IV",            "Male"
 "Václav",              "Male"
 "Jiří z Poděbrad",     "Male"
 "Jan Žižka",           "Male"
 "Jan Hus",             "Male"
 "Záviš z Falknštejna", "Male"
 "Libuše",              "Female"
 "Kunhuta",             "Female"
 "Alžběta Pomořanská",  "Female"
 "Eliška Přemyslovna",  "Female"
 "Anežka",              "Female"
 "T. G. Masaryk",       "Male"
 "Edvard Beneš",        "Male"
 "Václav Havel",        "Male"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Anarchy",         _("Usurper %s"),      _("?female:Usurper %s")
 "Communism",       _("General Secretary %s"), _("?female:General Secretary %s")
 "Despotism",       _("Voivode %s"),     _("?female:Voivode %s")
 "Fundamentalism",  _("Prophet %s"),     _("Prophetess %s")
}

flag = "czech"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="slovakian", "silesian", "moravian", "sorbian"

cities =
        "Praha", "Brno", "Ostrava", "Plzeň", "Hradec Králové",
        "Olomouc", "České Budějovice", "Ústí nad Labem", "Opava",
        "Most", "Pardubice", "Jihlava", "Chomutov", "Přerov",
        "Teplice", "Frýdek Místek", "Znojmo", "Cheb", "Zlín",
        "Karlovy Vary", "Uherské Hradiště", "Kolín", "Hodonín",
        "Stará Boleslav", "Příbram", "Šumperk", "Písek",
        "Litoměřice", "Třebíč", "Vyškov", "Kroměříž", "Klatovy",
        "Havlíčkův Brod", "Prostějov", "Chrudim", "Louny", "Děčín",
        "Rokycany", "Náchod", "Beroun", "Rakovník", "Mělník",
        "Jičín", "Tachov", "Strakonice", "Kutná Hora",
        "Bruntál", "Trutnov", "Sokolov", "Pelhřimov", "Nymburk",
        "Svitavy", "Ústí nad Orlicí", "Nový Jičín", "Tábor",
        "Domažlice", "Jindřichův Hradec", "Česká Lípa", "Benešov",
        "Liberec", "Rychnov nad Kněžnou", "Český Krumlov",
        "Prachatice", "Semily", "Žďár nad Sázavou", "Vsetín",
        "Osek", "Litomyšl", "Velehrad", "Těšín", "Rožmberk",
        "Tovačov", "Sezimovo Ústí", "Hořice", "Kouřim",
        "Poděbrady", "Vilémov", "Kunvald", "Dvůr Králové",
        "Bezděz", "Třeboň", "Šternberk", "Sázava", "Slaný",
        "Mladá Boleslav", "Kunštát", "Zelená Hora", "Duchcov",
        "Žatec", "Kladsko", "Horažďovice", "Čáslav", "Pirkštejn",
        "Krnov", "Rožmitál", "Loket", "Kladno",
        "Jablonec nad Nisou", "Břeclav", "Blansko", "Karviná"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
