# Freeciv(nation) · pontic

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/pontic.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的pontic定义

## 正文
```ruleset
[nation_pontic]

name=_("Pontic")
plural=_("?plural:Pontians")
groups="Ancient", "Medieval", "Asian"
legend=_("Pontus is a region on the Black Sea coast of Asia Minor,\
 currently part of Turkey but historically part of the Greek cultural\
 realm. A Hellenistic Kingdom of Pontus was founded in the 3rd century\
 BCE, which reached its greatest splendor under Mithridates the Great\
 before succumbing to Rome. After centuries of Roman and Byzantine rule,\
 Pontus became an independent state again when in 1204 the Empire of\
 Trebizond was founded as one of the successors of the crumbling\
 Byzantine Empire. Under the Komnenos dynasty, Trebizond held out as the\
 very last remnant of the Roman Empire until it finally fell to the\
 Ottomans in 1461. During the Turkish-Greek population transfers after\
 World War I, most Pontic Greeks were deported, and today the population\
 of Pontus is almost exclusively Turkish.")

leaders = {
 "name",                       "sex"
 "Iason",                      "Male"
 "Mithridatis I Ktistis",      "Male"
 "Mithridatis VI Megas",       "Male"
 "Alexios I Megas Komninos",   "Male"
 "Alexios III Megas Komninos", "Male"
 "Anna Megali Komnini",        "Female"
 "David Megas Komninos",       "Male"
 "Efkleidis Kourtidis ",       "Male"
}

ruler_titles = {
 "government",   "male_title",       "female_title"
 "Anarchy",      _("Usurper %s"),    _("?female:Usurper %s")
 "Democracy",    _("Chancellor %s"), _("?female:Chancellor %s")
 "Despotism",    _("Despot %s"),     _("?female:Despot %s")
}

flag="trebizond"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "Bosporan", "Armenian", "Georgian"

cities =
 "Trapezounta",
 "Sinopi",
 "Amisos",
 "Amaseia",
 "Kerasounta",
 "Kotyora",
 "Euchaita",
 "Riza",
 "Themiskyra",
 "Chersonisos Tauriki",
 "Herakleia Pontiki",
 "Fasis",
 "Olbia Pontiki",
 "Sebastoupolis",
 "Ta Kabeira",
 "Tanais",
 "Pantikapaion",
 "Odessos",
 "Dazimon",
 "Kamacha",
 "Dioskourias",
 "Amastris",
 "Kios",
 "Gangra",
 "Gazioura",
 "Farnakeia",
 "Koloneia",
 "Zela",
 "Kaloupini",
 "Tieion",
 "Magnopolis",
 "Patara",
 "Bathys",
 "Nikopolis",
 "Satala",
 "Komana Pontiki",
 "Neapolis",
 "Eupatoria",
 "Laodikeia Pontiki",
 "Tyras",
 "Santi",
 "Tripolis",
 "Kalos Limen",
 "Talaura"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
