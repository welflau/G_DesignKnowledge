# Freeciv(nation) · samnite

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/samnite.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的samnite定义

## 正文
```ruleset
[nation_samnite]

name=_("Samnite")
plural=_("?plural:Samnites")
groups="Ancient", "European"
legend=_("The Samnites were an ancient confederation of Italic tribes who\
 spoke the Oscan language and inhabited Central Italy, South of the\
 Sabines. After losing the wars with Rome the Samnites were subjected to\
 Rome and became Romanized. They were good soldiers and famed as Roman\
 gladiators.")
leaders = {
 "name",                 "sex"
 "Statius",              "Male"
 "Gellius Egnatius",     "Male"
 "Gaius Papius Mutilus", "Male"
 "Gaius Pontius",        "Male"
 "Ofilius Calavius",     "Male"
 "Ovius Calavius",       "Male"
 "Novius Calavius",      "Male"
}
flag="samnium"
flag_alt = "rome"
style = "Classical"
ruler_titles = {
 "government",      "male_title",      "female_title"
 "Anarchy",         _("Usurper %s"),   _("?female:Usurper %s")
 "Democracy",       _("Tribune %s"),   _("?female:Tribune %s")
 "Republic",        _("Consul %s"),    _("?female:Consul %s")
}
init_techs=""
init_buildings=""
init_units=""

conflicts_with="Western Roman", "Ostrogothic", 
               "Neapolitan", "Papal", "Italian" ;Langobardic
civilwar_nations = "Sabine", "Roman"

cities =
"Beneventum",
"Allifae",
"Aeclanum",
"Abellinum",
"Compsa",
"Aquilonia",
"Romulea",
"Trivicum",
"Equus Tuticus",
"Saepinum",
"Aesernia",
"Murgantia",
"Vescellium",
"Vercellium",
"Sicilinum",
"Ferentinum",
"Fratulum",
"Taurasia",
"Aletrium",
"Iuvanum",
"Caudium",
"Caiatia",
"Trebula",
"Cubulteria",
"Thermulae",
"Praetutii",
"Anxanum",
"Pallanum",
"Ortona",
"Histonium",
"Buca",
"Interamna",
"Larinum",
"Annum",
"Uscosium",
"Clotoris",
"Atessa",
"Venafrum",
"Saticula",
"Telesia",
"Bovianum Undecumanorum"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
