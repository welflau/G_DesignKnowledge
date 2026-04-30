# Freeciv(nation) · acadian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/acadian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的acadian定义

## 正文
```ruleset
[nation_acadian]

name=_("Acadian")
plural=_("?plural:Acadians")
groups="American"
legend=_("Acadia was first founded in 1604 as the first French colony in\
 North America. It was soon caught in the crossfire of French-English\
 wars, leading Acadia to change hands frequently. This led Acadians to\
 develop a separate identity and a form of self-government. Their lack of\
 support for any side in these wars earned them the title of French\
 neutrals, but also the distrust of British colonial authorities who\
 would forcefully deport them in 1755. Acadians have since returned to\
 their land and rebuilt.")

leaders = {
 "name",                        "sex"
 "Louis J. Robichaud",          "Male"
 "Beausoleil",                  "Male"
 "Pierre Dugua de Mons",        "Male"
 "Françoise-Marie Jacquelin",   "Female"
 "Charles de La Tour",          "Male"
 "Charles de Menou d'Aulnay",   "Male"
 "Jean de Poutrincourt",        "Male"
 "Pierre Amand Landry",         "Male"
 "François-Marcel Richard",     "Male"
 "Pascal Poirier",              "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Democracy",       _("Premier %s"),      _("Premiere %s")
 "Fundamentalism",  _("Abbot %s"),        _("Mother Superior %s")
}

flag="acadia"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="canadian"
civilwar_nations="newfoundland", "quebecois", "metis"

cities =
"Port-Royal",
"Caraquet",
"Bathurst", 
"Pubnico", 
"Shédiac", 
"Memramcook", 
"Moncton", 
"Clare", 
"Lamèque", 
"Cap-Pelé", 
"Miscou", 
"Grand-Sault",
"Chéticamp", 
"Saumarez", 
"Balmoral", 
"Néguac", 
"Shippagan", 
"Bas-Caraquet", 
"Beresford", 
"Charlo", 
"Bouctouche", 
"Petit-Rocher", 
"Dalhousie", 
"Baie-Sainte-Anne", 
"Tracadie", 
"Saint-Louis-de-Kent", 
"Inkerman", 
"New Bandon", 
"Richibouctou", 
"Beaubassin", 
"Notre-Dame-de-Kent", 
"Campbellton", 
"Grande-Anse", 
"Chipoudy", 
"Eldon", 
"Paquetville", 
"Pokemouche", 
"Abrams Village", 
"Rogersville", 
"Acadieville", 
"Saint-Isidore", 
"Saint-Paul", 
"Saint-Hilaire", 
"Dieppe", 
"Saint-Quentin", 
"Notre-Dame-de-Lourdes", 
"Pointe-Verte", 
"Saint-André", 
"Edmundston", 
"Baker-Brook", 
"Clair", 
"Saint-Léolin", 
"Kedgwick", 
"Allardville", 
"Atholville", 
"Saint-Léonard", 
"Saint-Antoine", 
"Saint-Basile", 
"Rivière-Verte", 
"Nigadoo", 
"Maisonnette", 
"Carleton", 
"Addington", 
"Drummond", 
"Saint-Joseph", 
"Saint-Jacques", 
"Rivière-du-Portage", 
"Eel River Crossing", 
"Saint-Charles", 
"Sainte-Anne-de-Kent", 
"Sainte-Anne-de-Madawaska", 
"Bertrand", 
"Saint-François-de-Madawaska", 
"Lac-Baker", 
"Sainte-Marie–Saint-Raphaël", 
"Le Goulet",
"Saint-Pierre",
"Miquelon"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
