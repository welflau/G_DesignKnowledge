# Freeciv(nation) · friulian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/friulian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的friulian定义

## 正文
```ruleset
[nation_friulian]

name=_("Friulian")
plural=_("?plural:Friulian")
groups="European", "Medieval"
legend=_("Friuli is a region in north-eastern Italy. A duchy of the Lombards\
 and then a march of the Franks, it was ruled by the Patriarchs of Aquileia\
 from the 11th century onward. In the 15th century Friuli was divided between\
 Venice and Austria. The Friulian language is closely related to the Romansh\
 language spoken in Switzerland.")

leaders = {
 "name",                         "sex"
 "Gisulf",                       "Male"
 "Baldric",			 "Male"
 "Sigeard di Beilstein",	 "Male"
 "Marquart di Randelle",	 "Male"
 "Luigi Faidutti",               "Male"
 "Josef Marchet",		 "Male"
 "Tiziano Tessitori",		 "Male"
}

flag="friuli"
flag_alt = "-"
style = "European"

ruler_titles = { "government",     "male_title",       "female_title"
                 "Despotism",      _("Margrave %s"),   _("Margravine %s")
                 "Fundamentalism", _("Patriarch %s"),  _("Matriarch %s")
	       }

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "venetian", "slovenian", "romansh"

cities =
 "Aquilee (ocean)",
 "Udin (plains)",
 "Cividât",
 "Pordenon",
 "Gurize",
 "Gardiscje",
 "Monfalcon",
 "Sacîl",
 "Concuardie",
 "Cordenons",
 "Codroip",
 "Purcie",
 "Daçan di Pordenon",
 "Tavagnà",
 "San Vît dal Tiliment",
 "Tisane",
 "Çarvignan",
 "Spilimberc",
 "Cjampfuarmit",
 "Roncjis di Monfalcon",
 "Vile di Flum",
 "Glemone",
 "Manià",
 "Fontanefrede",
 "Tumieç",
 "Davian",
 "Tarcint",
 "Brugnere",
 "Pasian di Prât",
 "Grau",
 "Cjasarse",
 "Prate",
 "Lignan",
 "San Denêl",
 "Çopule",
 "Cormons",
 "Tresesin",
 "Pasian di Pordenon",
 "San Zorç di Noiâr",
 "Staranzan",
 "Buie",
 "Puçui",
 "Manzan",
 "San Canzian",
 "Cjanive di Sacîl",
 "Siest",
 "Maian",
 "Remanzâs",
 "Feagne",
 "Lavorêt",
 "Tarvis",
 "San Zorç da la Richinvelde",
 "Ponteibe"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
