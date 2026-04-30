# Freeciv(nation) · walloon

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/walloon.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的walloon定义

## 正文
```ruleset
[nation_walloon]

name=_("Walloon")
plural=_("?plural:Walloons")
groups="European"
legend = _("The Walloons are the French speaking inhabitants of Belgium.\
 In the 19th century, Wallonia was first region on the European\
 continent to industrialize and the second in the world after England.\
 It subsequently became a hotbed of socialist and labor union activity.")

leaders = {
 "name",                        "sex"
 "Baudouin de Constantinople",  "Male"
 "Godefroid de Bouillon",       "Male"
 "Jacqueline de Hainaut",       "Female"
 "Maximilien-Henri de Bavière", "Male"
 "Jules Destrée",               "Male"
 "Léon Degrelle",               "Male"
 "Julien Lahaut",               "Male"
 "Elio Di Rupo",                "Male"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Communism",       _("Chairman %s"),       _("Chairwoman %s")
 "Fundamentalism",  _("Prince-Bishop %s"),  _("Princess-Bishop %s")
 "Despotism",       _("Count %s"),          _("Countess %s")
 "Republic",        _("Stadtholder %s"),    _("Stadtholdress %s")
}

flag="wallonia"
flag_alt = "belgium"
style = "european"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="german belgian", "luxembourgish", "liege"

cities =
 "Namur (river)",
 "Charleroi (river)",
 "Liège (river, hills)",
 "Mons (hills)",
 "La Louvière",
 "Tournai",
 "Seraing (river, forest, hills)",
 "Verviers (hills, forest)",
 "Mouscron",
 "Châtelet (river)",
 "Binche",
 "Wavre",
 "Louvain-la-Neuve",
 "Ath",
 "Arlon (hills)",
 "Soingies",
 "Andenne (river, hills)",
 "Nivelles",
 "Saint-Ghislain",
 "Fleurus",
 "Gembloux",
 "Braine-le-Comte",
 "Huy (river, hills)",
 "Eupen (hills, forest)",
 "Lessines",
 "Comines-Warneton",
 "Walcourt",
 "Marche-en-Famenne (hills, forest)",
 "Péruwelz",
 "Visé (river, hills)",
 "Herve",
 "Fontaine-l'Evêque",
 "Ciney",
 "Thuin",
 "Hannut",
 "Bastonge (mountains, hills)",
 "Genappe",
 "Waremme",
 "Couvain",
 "Leuze-en-Hainaut",
 "Dinant (river, hills)",
 "Jodoigne",
 "Rochefort",
 "Enghien",
 "Malmedy (hills, mountains)",
 "Virton (hills, forest)",
 "Spa (hills)",
 "Durbuy (hills)",
 "Chimay",
 "Fosses-la-Ville",
 "Saint-Vith (mountains, hills, forest)",
 "Beauraing",
 "Philippeville",
 "Le Rœulx",
 "Antoing",
 "Beaumont",
 "Stavelot (hills, mountains)",
 "Neufchâteau (hills)",
 "Chièvres",
 "Saint-Hubert (hills)",
 "Limbourg (hills)",
 "Bouillon (river, hills, forest)",
 "Florenville",
 "Chiny (hills)",
 "Houffalize (mountains, hills)",
 "La Roche-en-Ardenne (hills)"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
