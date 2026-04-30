# Freeciv(nation) · macedonian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/macedonian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的macedonian定义

## 正文
```ruleset
[nation_macedonian]

name=_("Macedonian")
plural=_("?plural:Macedonians")
groups="Modern", "European"
legend=_("The Republic of Macedonia is located in the south-central part\
 of the Balkan peninsula. It declared independence from Yugoslavia in\
 1991.")

leaders = {
 "name",                        "sex"
 "Marko Mrnjavčević",           "Male"
 "Christo Matov",               "Male"
 "Dame Gruev",                  "Male"
 "Nikola Karev",                "Male"
 "Gotze Delchev",               "Male"
 "Metodija Andonov-Čento",      "Male"
 "Lazar Koliševski",            "Male"
 "Kiro Gligorov",               "Male"
}
ruler_titles = {
 "government",      "male_title",        "female_title"
 "Despotism",       _("Voivode %s"),     _("?female:Voivode %s")
 "Fundamentalism",  _("Patriarch %s"),   _("Matriarch %s")
}

flag="macedonia"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="bulgarian", "albanian", "serbian"

; http://de.wikipedia.org/wiki/Liste_der_Städte_in_Mazedonien
cities =
 "Skopje", 
 "Kumanovo",
 "Bitola",
 "Prilep",
 "Tetovo",
 "Veles",
 "Ohrid",
 "Gostivar",
 "Štip",
 "Strumica",
 "Kavadarci",
 "Struga",
 "Kočani",
 "Kičevo",
 "Lipkovo",
 "Želino",
 "Saraj",
 "Radoviš",
 "Tearce",
 "Kriva Palanka",
 "Gevgelija",
 "Negotino",
 "Sveti Nikole",
 "Studeničani",
 "Vinica",
 "Debar",
 "Negotino-Pološko",
 "Delčevo",
 "Resen",
 "Ilinden",
 "Brvenica",
 "Kamenjane",
 "Bogovinje",
 "Berovo",
 "Aračinovo",
 "Probištip",
 "Čegrane",
 "Bosilovo",
 "Vasilevo",
 "Zajas",
 "Valandovo",
 "Novo Selo",
 "Kondovo",
 "Dolneni",
 "Oslomej",
 "Kratovo",
 "Dolna Banjica"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
