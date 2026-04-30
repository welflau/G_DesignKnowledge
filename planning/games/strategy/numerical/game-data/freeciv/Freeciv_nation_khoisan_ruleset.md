# Freeciv(nation) · khoisan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/khoisan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的khoisan定义

## 正文
```ruleset
[nation_khoisan]

name=_("Khoisan")
plural=_("?plural:Khoisan")
groups="Ancient", "African"
legend=_("Khoisan speakers are typically divided between the Khoikhoi,\
 traditionally herders, and the San, traditionally hunter gatherers.\
 They are traditionally among the most egalitarian societies on the\
 planet. San society in particular is organized around the institutions\
 of family and band. Khoisan peoples carry some of the most ancient\
 genetic lineages in the world. Today there are over 300,000 Khoisan\
 people, forming significant minorities in and around the Kalahari desert\
 in Namibia, Botswana, South Africa, and Angola.")

leaders = {
"name", 			"sex"
"!U", 				"Male"
"Krotoa", 			"Male"
"╪Toma", 			"Male"
"/Gawamūma /Ōnōb", 		"Male"
"Tsamgao", 			"Male"
"╪Gao", 			"Male"
"/Ti!kay", 			"Male"
"Adam Kok III", 		"Male"
"Manasse ǃNoreseb Gamab", 	"Male"
"DaSo", 			"Female"
}

flag="khoisan"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "namibian", "xhosa"

cities =
"//Hui !Gaeb",
"Khorixas",
"Gam",
"Hoachanas",
"Seeis",
"ǀAiǁGams",
"!Hoaxa !nâs",
"Keitsa",
"Cho/ana",
"Khumsa",
"!No!Go",
"Nama",
"//Gon//Gana",
"Kai Kai",
"Dom!Na",
"Khownwa",
"╪Go╪Gowe",
"Nam Tchoha",
"//No!Gau",
"Kautsa",
"Gura",
"Khumsa",
"Gautscha",
"Khaxutsus",
"Tsumkwe",
"//Khara hais",
"!Huni //hāb",
"Huri ╪oaxa",
"Gūdaos",
"Kai mûs",
"!Gariep"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
