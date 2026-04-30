# Freeciv(nation) · yucatecan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/yucatecan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的yucatecan定义

## 正文
```ruleset
[nation_yucatecan]

name=_("Yucatecan")
plural=_("?plural:Yucatecans")
groups="American"
legend=_("Yucatán is a peninsula of Mexico, famous for its Maya heritage\
 and its white beaches. Its name is often claimed to mean \"we don't\
 understand you\" in Yucatec Maya. On two occasions in the 19th century\
 Yucatán declared independence from Mexico. Currently it is divided into\
 three states: Yucatán, Campeche and Quintana Roo.")

leaders = {
 "name",                        "sex"
 "Francisco de Montejo",        "Male"
 "Diego de Landa",              "Male"
 "Andrés Quintana Roo",         "Male"
 "Santiago Méndez",             "Male"
 "Miguel Barbachano",           "Male"
 "Justo Sierra",                "Male"
 "Felipe Carrillo Puerto",      "Male"
 "Víctor Cevera Pacheco",       "Male"
 "Carlos Sansores Pérez",       "Male"
 "Ivonne Ortega",               "Female"
}
ruler_titles = {
 "government",      "male_title",            "female_title"
 "Despotism",       _("Captain General %s"), _("?female:Captain General %s")
 "Fundamentalism",  _("Bishop %s"),          _("Mother Superior %s")
}

flag="yucatan"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "mayan"

cities =
 "Mérida (jungle, forest)",
 "Campeche (ocean)",
 "Chetumal (ocean, swamp)",
 "Valladolid (forest, jungle)",
 "Tekax (jungle, forest, hills)",
 "Izamal",
 "Maní",
 "Sisal (ocean)",
 "Cancún (ocean, jungle)",
 "Ciudad del Carmen (ocean, swamp)",
 "Champotón (ocean)",
 "San Miguel (ocean)",		;Cozumel
 "Playa del Carmen (ocean)",
 "Bacalar (lake, jungle)",
 "Celestún (swamp)",
 "Escárcega",
 "Motul",
 "Ticul",
 "Progreso (ocean)",
 "Tizimín",
 "Kanasín",
 "Tulum (ocean)",
 "Akumal",
 "Oxkutzcab",
 "Chicxulub",
 "Peto (jungle)",
 "Xpujil (jungle)",
 "Umán",
 "Felipe Carrillo Puerto",	;Chan Santa Cruz
 "Candelaria (river, swamp)",
 "Isla Mujeres (ocean)",
 "Dzemul",
 "Muna",
 "José María Morelos",
 "Kantunilkín",
 "Mahahual",
 "Xcalak",
 "Calkiní",
 "Hecelchakán",
 "Hopelchén (jungle)",
 "Palizada",
 "Tenabo",
 "Río Lagartos (river, swamp)",
 "Telchac Puerto (ocean)",
 "Telchac Pueblo (!ocean)",
 "Dzitbalché",
 "Bolonchén",
 "Zoh Laguna",
 "Punta Allen (ocean)",		;Javier Rojo Gómez
 "Tecoh",
 "Komchén",
 "Seybaplaya (ocean)",
 "Chiná",
 "Xelhá (ocean)",
 "Yucalpetén",
 "San Felipe",
 "Pisté",
 "Conkal",
 "Alfredo V. Bonfil"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
