# Freeciv(nation) · saintlucian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/saintlucian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的saintlucian定义

## 正文
```ruleset
[nation_saintlucian]

name=_("Saint Lucian")
plural=_("?plural:Saint Lucian")
groups="Modern", "American"
legend=_("Saint Lucia is an island nation in the Eastern Caribbean. During\
 the colonial era, Saint Lucia changed hands between France and Britain no\
 less than fourteen times until the British finally secured it in 1814. The\
 island became independent in 1979. It a member both of the Commonwealth\
 and La Francophonie. The economy is based on tourism, bananas and sugar.")

leaders = {
 "name",                   "sex"
 "François le Clerc",      "Male"
 "Jean-Baptiste Lacrosse", "Male"
 "George L. Charles",      "Male"
 "William Arthur Lewis",   "Male"
 "John Compton",           "Male"
 "Pearlette Louisy",       "Female"
}

ruler_titles = {
 "government",      "male_title",    "female_title"
 "Fundamentalism",  _("Bishop %s"),  _("Mother Superior %s")
}
flag="saint_lucia"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Barbadian", "Vincentian" ; martinican

cities =
 "Castries",
 "Gros Islet",
 "Vieux Fort",
 "Micoud",
 "Dennery",
 "Laborie",
 "Anse-la-Raye",
 "Soufrière",
 "Choiseul",
 "Canaries",
 "Bexon",
 "Grande Riviere",
 "Babonneau",
 "Augier",
 "Ciceron",
 "Corinthe",
 "Morne du Don",
 "Marisule",
 "Marchand",
 "Bois d'Orange",
 "La Clery",
 "Dasruisseaux",
 "Au Leon",
 "Le Croix Maingot",
 "La Resource",
 "Balata",
 "Blanchard",
 "The Morne",
 "Bois Patat",
 "Rock Hall",
 "Entrepot",
 "Ti Rocher",
 "Sans Souci",
 "Bocage",
 "Mon Repos",
 "Shanty Town",
 "Derniere Riviere",
 "Coolie Town",
 "New Development",
 "Bishop's Gap",
 "Cap Estate",
 "Cas en Bas",
 "By Pass",
 "Cul de Sac",
 "Patience",
 "Leslie Land",
 "Saint Jude's Highway",
 "Choc",
 "Marc Marc",
 "Saltibus"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
