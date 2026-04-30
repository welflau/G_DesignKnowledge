# Freeciv(nation) · boer

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/boer.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的boer定义

## 正文
```ruleset
[nation_boer]

name=_("Boer")
plural=_("?plural:Boers")
groups= "African"
legend=_("The Boers were descendants of Dutch colonists who settled in\
 South Africa after 1650 CE. After migrating into the hinterland after the\
 British takeover of South Africa, they briefly controlled a number of\
 republics, including the Transvaal and the Orange Free State, before\
 being defeated by the British in the war of 1899-1902.")

leaders = {
 "name",                "sex"
 "Jan van Riebeeck",    "Male"
 "Wessel Pretorius",    "Male"
 "Piet Retief",         "Male"
 "Racheltjie de Beer",  "Female"
 "Andries Pretorius",   "Male"
 "Paulus Kruger",       "Male"
 "Louis Botha",         "Male"
 "Jan Smuts",           "Male"
 "Hendrik Verwoerd",    "Male"
 "Pik Botha",           "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Despotism",       _("General %s"),         _("?female:General %s")
 "Fundamentalism",  _("Reverend %s"),        _("?female:Reverend %s")
 "Republic",        _("State President %s"), _("?female:State President %s")
}

flag="boer"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "dutch"

cities =
 "Kaapstad",
 "Stellenbosch",
 "Swellendam",
 "Graaff-Reinet",
 "Johannesburg",
 "Oudtshoorn",
 "Vereeniging",
 "Bloemfontein",
 "Welkom",
 "Bethlehem",
 "Nieu-Bethesda",
 "Pretoria",
 "De Aar",
 "Middelburg",
 "Springbok",
 "Uitenhage",
 "Paarl",
 "Potchefstroom",
 "Leliesfontein",
 "Nelspruit",
 "Pietermaritzburg",
 "Lydenburg",
 "Ermelo",
 "Klerksdorp",
 "Vryburg",
 "Hotazel",
 "Postmasburg",
 "Pofadder",
 "Kenhardt",
 "Vanrhynsdorp",
 "Bitterfontein",
 "Potgietersrus",
 "Waterkloof",
 "Utrecht",
 "Piet Retief",
 "Potchefstroom",
 "Winburg",
 "Rooigrond",
 "Vryheid"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
