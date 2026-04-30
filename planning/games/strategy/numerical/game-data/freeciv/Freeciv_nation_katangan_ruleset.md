# Freeciv(nation) · katangan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/katangan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的katangan定义

## 正文
```ruleset
[nation_katangan]

name=_("Katangan")
plural=_("?plural:Katangans")
groups="African"
legend=_("Katanga, the southernmost part of the Democratic Republic of\
 the Congo, rich in minerals and once home to the Yeke Kingdom. The\
 region seceded from Congo a few days after that country's independence\
 from Belgium in 1960. The state, protected by Belgian mining\
 industrialists and foreign mercenaries, was led by Moise Tshombe.\
 Katanga was reincorporated into Congo after a Congolese and UN military\
 campaign.")
leaders = {
 "name",                "sex"
 "Msiri",	        "male"
 "Moïse Tshombe",	"male"
 "Godefroid Munongo",   "male"
}

flag="katanga"
flag_alt = "-"
style = "tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "congolese", "angolan"

cities =
 "Élisabethville",	;Lubumbashi
 "Albertville",		;Kalemie
 "Kolwezi",
 "Kamina",
 "Bunkeya",
 "Jadotville",		;Likasi
 "Bukama",
 "Manono",
 "Baudouinville",	;Moba
 "Kipushi",
 "Niemba",
 "Dilolo",
 "Sakania",
 "Kambove",
 "Kongolo",
 "Kabalo",
 "Kabongo",
 "Kaniama",
 "Mulongo",
 "Balamba",
 "Nyunzu",
 "Tenke",
 "Kipamba",
 "Malemba-Nkulu",
 "Lubudi",
 "Pweto",
 "Mokambo",
 "Kasenga",
 "Kanteba",
 "Luambo",
 "Sandoa",
 "Mutshatsha",
 "Kole",
 "Mitwaba",
 "Kapanga"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
