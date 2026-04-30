# Freeciv(nation) · paraguayan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/paraguayan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的paraguayan定义

## 正文
```ruleset
[nation_paraguayan]

name=_("Paraguayan")
plural=_("?plural:Paraguayans")
groups="Modern", "American"
legend=_("Paraguay is located in the heartland of South America. It was\
 conquered by the Spanish in the late 16th century. The colony was mostly\
 controlled by the Jesuits until their expulsion in 1767. In 1811,\
 Paraguay was the first South American country to achieve independence\
 from Spain. A number of highly authoritarian rulers governed the country\
 as a tyranny but also turned it into a military and economic powerhouse.\
 The War of the Triple Alliance of 1864-1870 led to the near\
 annihilation of Paraguay, which lost half of its territory and eighty\
 per cent of its male population. Paraguay's history remains marked by\
 instability and authoritarianism, alhough it managed to defeat Bolivia\
 in the Chaco War of 1932-1936. For much of the 20th century the country\
 was ruled by General Stroessner, who provided a safe haven for Nazi war\
 criminals. Around the turn of the millennium however Paraguay started to\
 see a democratic system of government and an impressive economic growth.")

leaders = {
 "name",                        "sex"
 "Gaspar Rodríguez de Francia", "Male"
 "Carlos Antonio López",        "Male"
 "Francisco Solano López",      "Male"
 "Eusebio Ayala",               "Male"
 "José Félix Estigarribia",     "Male"
 "Higinio Moríñigo",            "Male"
 "Alfredo Stroessner",          "Male"
 "Andrés Rodríguez",            "Male"
 "Fernando Lugo",               "Male"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Communism",       _("Comandante %s"),  _("Comandanta %s")
 "Despotism",       _("Dictator %s"),    _("Dictatrix %s")
 "Fundamentalism",  _("Abbot %s"),       _("Mother Superior %s")
}

flag="paraguay"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="guarani"
civilwar_nations="guarani", "german"

cities =
 "Asunción",
 "Ciudad del Este",
 "Encarnación",
 "Coronel Oviedo",
 "San Pedro de Ycuamandiyú",
 "Caacupé",
 "Villarrica",
 "Concepción",
 "Pilar",
 "Paraguarí",
 "Pedro Juan Caballero",
 "Areguá",
 "Mariano Roque Alsonso",
 "Salto del Guairá",
 "Caazapá",
 "San Juan Bautista",
 "Caagazú",
 "Pozo Colorado",
 "Filadelfia",
 "Fuerte Olimpo",
 "Itá",
 "Santa Rita",
 "Villa Hayes",
 "San Estanislao",
 "San Ignacio",
 "Doctor Eulogio Estigarribia",
 "San Lorenzo",
 "Luque",
 "Capiatá",
 "Lambaré",
 "Fernando de la Mora",
 "Limpio",
 "Ñemby",
 "Fernheim",
 "Villa Elisa",
 "Villeta",
 "Hohenau",
 "Doctor Pedro P. Peña",
 "Nueva Italia",
 "Capitán Pablo Lagerenza",
 "Neufeld",
 "Itaguá",
 "Hernandaríaz",
 "Presidente Franco",
 "Minga Guazú",
 "Repatriación",
 "Marechal Estigarribia",
 "Nueva Germania"



```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
