# Freeciv(nation) · mauritanian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/mauritanian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的mauritanian定义

## 正文
```ruleset
[nation_mauritanian]

name=_("Mauritanian")
plural=_("?plural:Mauritanians")
groups="African", "Modern"
legend=_("Mauritania is a country in North West Africa, where the Arab\
 and Sub-Saharan African worlds meet. Mauritania became Islamized from\
 the 11th century onwards. Colonized by France in the 19th century, the\
 country became an independent republic in 1960.")

leaders = {
 "name",                        "sex"
 "Nasr ad-Din",                 "Male"
 "Ma al-'Aynayn",               "Male"
 "Moktar Ould Daddah",          "Male"
 "Maaouya Ould Sid'Ahmed Taya", "Male"
}

ruler_titles = {
 "government",     "male_title",   "female_title"
 "Monarchy",       _("Emir %s"),   _("Emira %s")
 "Fundamentalism", _("Imam %s"),   _("Imama %s")
}

flag="mauritania"
flag_alt = "-"
style = "babylonian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "sahrawi", "jolof", "amazigh"

cities =
 "Nawakshut (ocean)",
 "Kifa",
 "Nawadhibu (ocean)",
 "Al-Quwarib",
 "An-Na'ma",
 "Kayhaydi",
 "Buqa",
 "'Ayun-al-'Atrus",
 "Hsay Walad 'Ali Babi",
 "Al-Zwirat",
 "Tijiqja",
 "Atar",
 "Aqjawajat",
 "Bu Tilimit",
 "Tinbadgha",
 "Guérou",
 "Magta' Lahjar",
 "Alak",
 "Tintane",
 "Adel Bagru",
 "Walata",
 "Bababé",
 "Chagar",
 "Djowol",
 "M'bout",
 "Afdayrik",
 "Maghama",
 "Kubanni",
 "Shingati",
 "Arafat",
 "Benishab",
 "Choum",
 "Dar-Naim",
 "El Mina",
 "Ksar",
 "Ar-Riyadh",
 "Sebkha",
 "Tevragh-Zeina",
 "Teyarett",
 "Toujouonine"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
