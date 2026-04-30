# Freeciv(nation) · syrian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/syrian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的syrian定义

## 正文
```ruleset
[nation_syrian]

name=_("Syrian")
plural=_("?plural:Syrians")
groups="Modern", "Asian"
legend=_("The modern Syrian Arab Republic was formed from a French mandate\
 and gradually gained independence during the 1940s.")

leaders = {
 "name",                        "sex"
 "Taj al-Din al-Hasani",        "Male"
 "Hashim al-Atassi",            "Male"
 "Khalid al-Azm",               "Male"
 "Shukri al-Kuwatli",           "Male"
 "Hafez al-Assad",              "Male"
}

ruler_titles = {
 "government",     "male_title",              "female_title"
 "Despotism",      _("Sheikh %s"),            _("Shaykha %s")
 "Fundamentalism", _("Caliph %s"),            _("Calipha %s")
 "Monarchy",       _("Emir %s"),              _("Emira %s")
}

flag="syria"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

; Similar flags:
conflicts_with="iraqi"
civilwar_nations="turkish", "israeli", "lebanese"

; http://pl.wikipedia.org/wiki/Miasta_Syrii
cities =
 "Dimashq ash-Sham",	; Damascus
 "Halab",		; Aleppo
 "Hims",		; Homs
 "Hama",
 "Al-Ladhiqiya",	; Latakia
 "Dayr as-Zawr",
 "Ar-Raqqa",
 "Al-Bab",
 "Duma",
 "Safita",
 "Salamiya",
 "Tartous",
 "Ath-Thawra",
 "Al-Qamishli",
 "Al-Hasaka",
 "Dar'a",
 "Darayya",
 "Manbij",
 "Jabala",
 "Azaz",
 "As-Suwayda",
 "Abu Kamal",
 "At-Tall",
 "Al-Mayadin",
 "Nawa",
 "Ar-Rastan",
 "Tadmor",		; Palmyra
 "Ayn al-Arab",
 "Afrin",
 "Khan Shaykhun"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
