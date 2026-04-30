# Freeciv(nation) · luxembourgish

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/luxembourgish.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的luxembourgish定义

## 正文
```ruleset
[nation_luxembourgian]

name=_("Luxembourgish")
plural=_("?plural:Luxembourgians")
groups="European", "Medieval", "Modern"
legend=_("One of Europe's smaller countries, Luxembourg was founded as\
 a county in 963. In 1815 it was elevated to a Grand Duchy in a personal\
 union with the Netherlands, which was severed in 1890.")

leaders = {
 "name",                "sex"
 "Siegfried I",         "Male"
 "Heng de Blannen",     "Male"
 "Heinrich IV",         "Male"
 "Wenzel I",            "Male"
 "Sigismund",           "Male"
 "Karl V",              "Male"
 "Wëllem I",            "Male"
 "Wëllem III",          "Male"
 "Paul Eyschen",        "Male"
 "Marie-Adélaïde",      "Female"
 "Charlotte",           "Female"
 "Jean",                "Male"
}

ruler_titles = {
 "government",     "male_title",           "female_title"
 "Despotism",      _("Count %s"),          _("Countess %s")
 "Fundamentalism", _("Bishop %s"),         _("Mother Superior %s")
 "Monarchy",       _("Grand Duke %s"),     _("Grand Duchess %s")
 "Republic",       _("Stadtholder %s"),    _("Stadtholdress %s")
}

flag="luxembourg"
flag_alt = "netherlands"
style = "european"

init_techs=""
init_buildings=""
init_units=""
conflicts_with="dutch"
civilwar_nations="german belgian", "french", "walloon", "dutch"

cities =
 "Lëtzebuerg",		;Luxembourg
 "Ettelbréck",		;Ettelbrück
 "Dikrech",		;Diekirch
 "Iechternach",		;Echternach
 "Esch-Uelzecht",	;Esch-sur-Alzette
 "Miersch",		;Mersch
 "Wolz",		;Wiltz
 "Déifferdeng",		;Differdange
 "Gréiwemaacher",	;Grevenmacher
 "Diddeleng",		;Dudelange
 "Veianen",		;Vianden
 "Péiteng",		;Pétange
 "Réimech",		;Remich
 "Suessem",		;Sanem
 "Rëmeleng",		;Rumelange
 "Kapellen",		;Capellen
 "Klierf",		;Clervaux
 "Hesper",		;Hesperange
 "Beetebuerg",		;Bettembourg
 "Schëffleng",		;Schifflange
 "Keel",		;Kayl
 "Nidderkäerjeng",	;Bascharage
 "Mamer",		;Mamer
 "Walfer",		;Walferdange
 "Stroossen",		;Strassen
 "Bartreng",		;Bertrange
 "Monnerëch",		;Monnercange
 "Jonglënster",		;Junglinster
 "Nidderaanwen",	;Niederanven
 "Réiser",		;Roeser
 "Kielen",		;Kehlen
 "Steesel",		;Steinsel
 "Stengefort",		;Steinfort
 "Munnerëf",		;Mondorf-les-Bains
 "Rammerech",		;Rambrouch
 "Wëntger",		;Wincrange
 "Mäertert",		;Mertert
 "Dippech",		;Dippach
 "Fiels",		;Larochette
 "Fréiséng",		;Frisange
 "Réiden",		;Rédange
 "Schëtter",		;Schuttrange
 "Konter",		;Contern
 "Luerenzweiler",	;Lorentzweiler
 "Koplescht",		;Kopstal
 "Sandweiler",		;Sandweiler
 "Habscht",		;Hobscheid
 "Betzder",		;Betzdorf
 "Ëlwen",		;Troisvierges
 "Kolmer-Bierg",	;Colmar-Berg
 "Stadbriedemes",	;Stadtbrediumus
 "Waasserbëlleg",	;Wasserbillig
 "Wuermeldeng",		;Wormeldange
 "Esch-Sauer",		;Esch-sur-Sûre
 "Maarnech"		;Marnach

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
