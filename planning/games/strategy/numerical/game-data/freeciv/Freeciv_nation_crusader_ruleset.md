# Freeciv(nation) · crusader

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/crusader.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的crusader定义

## 正文
```ruleset
[nation_crusader]

name=_("Crusader")
plural=_("?plural:Crusaders")
groups="Asian", "Medieval"
legend=_("The Crusades were a series of wars in which European armies\
 tried to re-establish Christian control over the Holy Land. The First\
 Crusade was called by Pope Urban II in 1095. The crusaders managed to\
 wrestle control of much of the Levant from Muslim hands and established\
 a number of states led by noblemen from European Christian dynasties.\
 The most powerful of crusader states was the Kingdom of Jerusalem; other\
 states included the County of Tripoli, the Principality of Antioch and\
 the Country of Edessa. Later crusades were less successful. Muslim (Arab\
 and Turkic) armies managed to push back the Crusaders and the last\
 Crusader controlled city, Acre, fell to the Mamluks in 1291.")

leaders = {
 "name",                  "sex"
 "Godefroid de Bouillon", "Male"
 "Baudouin de Boulogne",  "Male"
 "Bohémond de Tarente",   "Male"
 "Mélisende",             "Female"
 "Richard Cœur de Lion",  "Male"
 "Guy de Lusignan",       "Male"
 "Jean de Brienne",       "Male"
 "Jean d'Ibelin",         "Male"
 "Lucie",                 "Female"
}

ruler_titles = {
 "government",     "male_title",                "female_title"
 "Anarchy",        _("Usurper %s"),             _("?female:Usurper %s")
 "Communism",      _("Brother %s"),             _("Sister %s")
 "Democracy",      _("Chancellor %s"),          _("?female:Chancellor %s")
 "Despotism",      _("Count %s"),               _("Countess %s")
 "Fundamentalism", _("Patriarch %s"),           _("Matriarch %s")
}

flag="jerusalem"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Knights Templar", "Arab", "Mamluk", "Armenian", "Seljuk", "Latin", "Cypriot"

conflicts_with="Israeli", "Israelite", "Lebanese", "Syrian"

cities =
; names in Old French
 "Jhérusalem",
 "Edessa",
 "Antioche",
 "Akko (ocean)",
 "Tyr (ocean)",
 "Tripoli (ocean)",
 "Tiberias",
 "Jaffa (ocean)",
 "Ascalon (ocean)",
 "Gibelet (ocean)",	; Byblos
 "Turbessel",
 "Sidon (ocean)",
 "Beyrout (ocean)",
 "Crac de l'Ospital",	; Krak des Chevaliers
 "Monréal",
 "Haifa (ocean)",
 "Nazareth",
 "Blanchegarde",
 "Ramla",
 "Césarée (ocean)",
 "Sainct Syméon",
 "Toron",
 "Mirabel",
 "Hébron",
 "Arsur",
 "Belvoir",
 "Crac des Moabites",
 "Ibelin",
 "Naples",		; Nablus
 "Banias",
 "Maraclea",
 "Bethlehem",
 "Adelon",
 "Caymont",
 "Montgisard",
 "Scandeleon",
 "Chastel Blanc",
 "Beaufort",

; Armenian Cicilia

 "Sis",
 "Tarse",
 "Layas",
 "Alexandrette",
 "Mélitène",
 "Marase",

; Kingdom of Cyprus

 "Nicosie",
 "Limassol",
 "Famagouste",
 "Paphos",
 "Gastria"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
