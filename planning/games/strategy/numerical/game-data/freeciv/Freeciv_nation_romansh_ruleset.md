# Freeciv(nation) · romansh

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/romansh.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的romansh定义

## 正文
```ruleset
[nation_rumantsch]

name=_("Romansh")
plural=_("?plural:Romansh")
groups= "European", "Medieval"
legend=_("The Rumantsch or Romansh people are inhabitants of the Swiss\
 canton of Grisons who speak Romansh, a Romance language that retains\
 some unique characteristics and with a rich oral tradition. Although\
 Romansh is one of the four national languages of Switzerland and\
 projects are being undertaken to save the language, it is\
 losing terrain as many of its speakers switch to German. Before the\
 Napoleonic Era, the Three Leagues of Grisons were the only territory\
 of Europe where decision making was organized by taking votes.")

leaders = {
 "name",             "sex"
 "Tello",            "Male"
 "Filip Gallicius",  "Male"
 "Placi a Spescha",  "Male"
 "Caspar Decurtins", "Male"
 "Peider Lansel",    "Male"
 "Heinrich Schmid",  "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Democracy",       _("Councillor %s"),      _("?female:Councillor %s")
 "Despotism",       _("Bailiff %s"),         _("?female:Bailiff %s")
 "Fundamentalism",  _("Bishop %s"),          _("Mother Superior %s")
}

flag="grisons"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations= "liechtensteiner", "friulian"

cities =
 "Cuira",
 "Tavau",
 "Glion",
 "Eigias",
 "Domat",
 "San Murezzan",
 "Claustra-Serneus",
 "Puschlev",
 "Zezras",
 "Termin",
 "Samedan",
 "Panaduz",
 "Vaz",
 "Tusaun",
 "Flem",
 "Maiavilla",
 "Aschera",
 "Roveredo",
 "Vaz sut",
 "Arosa",
 "Scuol",
 "Val Müstair",
 "Malans",
 "Mustér",
 "Favugn",
 "Puntraschigna",
 "Tujetsch",
 "Bregaglia",
 "Cazas",
 "Sievgia en il Partenz",
 "Sumvitg",
 "Schlarigna",
 "Breil",
 "Zernez",
 "Crusch en il Partenz",
 "Lags",
 "Trun",
 "Razén",
 "Curvalda",
 "Mesauc",
 "Luzein",
 "Trin",
 "Tumein",
 "Brüsch",
 "Casti",
 "Samignun",
 "Cunter en il Partenz",
 "Nueinas",
 "Schlans",
 "Silvaplauna",
 "Seglias",
 "La Punt-Chamues-ch",
 "Falera",
 "Spleia"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
