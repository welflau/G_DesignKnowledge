# Freeciv(nation) · formosan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/formosan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的formosan定义

## 正文
```ruleset
[nation_formosan]

name=_("Formosan")
plural=_("?plural:Formosans")
groups="Asian", "Ancient", "Medieval", "Early Modern"
; /* xgettext:no-c-format */
legend=_("Taiwan is home to fourteen officially recognized and twelve unrecognized tribes,\
 all of whom are traditionally speakers of a group of Austronesian languages\
 known as Formosan. Historical linguists consider the island to be the home\
 of the Austronesian family, as it is host to the most diverse set of Austronesian\
 languages. Many of the tribes are traditionally matrilineal. Starting in the 17th\
 century, European and East Asian colonists vied for control of the island,\
 encroaching on aboriginal lands. Today, Formosans constitute around 2%\
 of the population of Taiwan.")

leaders = {
"name", 		"sex"
"Ciwas Ali", 		"Female"
"Taccaran", 		"Male"
"Kamachat Maloe",	"Male"
"Paelabang Danapan", 	"Male"
"Mona Rudao", 		"Male"
"Kamachat Aslamie", 	"Male"
"Walis Pelin", 		"Male"
"George Psalmanazar",	"Male"
}

flag="formosan"
flag_alt="-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Taiwanese", "Cham", "Filipino"

cities =
"Baccluan",
"Mattau",
"Sinkan",
"Taraquang",
"Tevorang",
"Soulang",
"Favorolang",
"Tirosen",
"Taccariang",
"Dorcko",
"Vasikan",
"Gierim",
"Saccam",
"Verovorang",
"Dolatock",
"Pangsoya",
"Pimaba",
"Jilon",
"Danshui",
"Tivalukang",
"Tarokei",
"Tampsui",
"Zoatalay",
"Lichoco",
"Taparri",
"Kimaurri",
"Senar",
"Pantaos",
"Lona",
"Ulibulibuk",
"Bankio",
"Alipai",
"Pinaski",
"Tamalakaw",
"Rikabung",
"Puyuma",
"Peinan",
"Balangaw",
"Apapalo",
"Kasabakan",
"Katipul",
"Nirbuaqan",
"Sabaha Bakalas"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
