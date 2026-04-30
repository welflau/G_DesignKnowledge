# Freeciv(nation) · neapolitan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/neapolitan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的neapolitan定义

## 正文
```ruleset
[nation_neapolitan]

name=_("Neapolitan")
plural=_("?plural:Neapolitans")
groups="European", "Medieval", "Early Modern"
legend=_("For centuries the Kingdom of Naples was the largest country\
 on the Italian Peninsula. Many European powers showed interest in the\
 kingdom and its throne changed hands many times. After the Napoleonic\
 Era it was merged with the Kingdom of Sicily.")

leaders = {
 "name",                "sex"
 "Carlo 'e Angiò",      "Male"
 "Giovanna I",          "Female"
 "Carlo 'e Durazzo",    "Male"
 "Giovanna II",         "Female"
 "Ferrantino",          "Male"
 "Masaniello",          "Male"
 "Carlo 'e Parma",      "Male"
 "Gioacchino Murat",    "Male"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Despotism",       _("Count %s"),          _("Countess %s")
 "Fundamentalism",  _("Cardinal %s"),       _("Madre %s")
}

flag="naples"
flag_alt = "sicily"
style = "Classical"

init_techs=""
init_buildings=""

init_units=""
civilwar_nations = "sicilian", "italian"

cities =
 "Napule (ocean, mountains)",
 "Bari (ocean)",
 "Taranto (ocean)",
 "Reggio Calavria (ocean)",
 "Foggia",
 "Salierno (ocean)",
 "Pescara (ocean)",
 "Giugliano (ocean)",
 "Lecce (ocean)",
 "Catanzaro (ocean)",
 "Brinnese (ocean)",
 "Torre d''o Grieco (ocean)",
 "Pezzulo (ocean)",
 "Casoria",
 "Caserta",
 "L'Aquila (mountains, hills)",
 "Lamezia Terme",
 "Cusenza",
 "Putenza",
 "Altamura",
 "Castiellammare 'e Stabia (ocean)",
 "Afravola",
 "Cotrone (ocean)",
 "Matera",
 "Cerignola",
 "Marano",
 "Puortece",
 "Manfredonia (ocean)",
 "Avellino",
 "Bitonto (ocean)",
 "San Severo",
 "Molfetta (ocean)",
 "Teramo",
 "Chiete",
 "Ercolano",
 "Cava de' Tirreni (mountains, hills)",
 "Averza",
 "Battipaglia (ocean)",
 "Campobasso",
 "Scafati (ocean)",
 "Martina Franca",
 "Fresulone (river)",
 "Torre Nunziata (mountains)",
 "Avezzano",
 "Maddaloni",
 "Vasto (ocean)",
 "Formia (hills)",
 "Vibo Valentia (ocean)",
 "Cassino (mountains, hills)",
 "Termoli (ocean)",
 "Gaieta (hills, ocean)",
 "Gallipoli (ocean)",
 "Isernia",
 "Tropea",
 "Melfi",
 "Surriente (ocean)",
 "Trani (ocean)",
 "Castrovillari",
 "Pizzo"



```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
