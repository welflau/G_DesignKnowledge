# Freeciv(nation) · assyrian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/assyrian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的assyrian定义

## 正文
```ruleset
[nation_assyrian]

name=_("Assyrian")
plural=_("?plural:Assyrians")
groups="Ancient", "Asian"
legend=_("Assyria was an empire in northern Mesopotamia, named after its\
 capital Ashur.")

leaders = {
 "name",                "sex"
 "Ashurbanipal",        "Male"
 "Tiglat Pileser III",  "Male"
 "Ashurnasirpal II",    "Male"
 "Shamiram",            "Female"
 "Agha Petros",         "Male"
 "Naoum Faik",          "Male"
}

ruler_titles = {
 "government",     "male_title",        "female_title"
 "Anarchy",        _("Usurper %s"),     _("?female:Usurper %s")
}

flag = "assyria"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="babylonian", "israelite", "aramean", "mitanni"

cities =
 "Ashur",
 "Nineveh",
 "Kalhu",
 "Arbela",
 "Edessa",
 "Osrhoene",
 "Nisibin",
 "Alqosh",
 "Urmia",
 "Kirkuk",
 "Akkad",
 "Mosul",
 "Dohuk",
 "Aqra",
 "Zibar",
 "Supna",
 "Zakho",
 "Hakkari",
 "Bohtan",
 "Ayn-Slibo",
 "Omed",
 "Tur-Abdin",
 "Merdo",
 "Tella-Shleela",
 "Kharput",
 "Perin",
 "Urhoy",
 "Ayn-Towo",
 "Salamas",
 "Khabour",
 "Malatya"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
