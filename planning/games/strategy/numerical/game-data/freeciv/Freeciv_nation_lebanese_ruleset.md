# Freeciv(nation) · lebanese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/lebanese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的lebanese定义

## 正文
```ruleset
[nation_lebanese]

name = _("Lebanese")
plural = _("?plural:Lebanese")
groups="Asian", "Modern"
legend=_("Located in the Levant, the Eastern shore of the Mediterranean,\
 Lebanon houses some of the oldest traces of human civilization. The old\
 homeland of the Phoenicians, Lebanon has since been ruled by many\
 empires. It was part of the Ottoman Empire for over four centuries and\
 became a French mandate after World War I. Lebanon proclaimed its\
 independence in 1943.")

leaders = {
 "name",                "sex"
 "Fakhr-al-Din II",     "Male"
 "Bashir Shihab II",    "Male"
 "Charles Debbas",      "Male"
 "Camille Chamoun",     "Male"
 "Fuad Chehab",         "Male"
 "Elie Hobeika",        "Male"
 "Rashid Karami",       "Male"
 "Rafiq Hariri",        "Male"
}

ruler_titles = {
 "government", "male_title",              "female_title"
 "Communism",  _("Secretary General %s"), _("?female:Secretary General %s")
 "Despotism",  _("General %s"),           _("?female:General %s")
 "Monarchy",   _("Emir %s"),              _("Emira %s")
}

flag = "lebanon"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="phoenician"
civilwar_nations="israeli", "syrian"

cities =
 "Bayrut",		;Beirut
 "Tarabulus",		;Tripoli
 "Ba'labakk",		;Baalbek
 "Sayda",		;Sidon
 "Al-Nabatiya",		;Nabatieh
 "Sur",			;Tyre
 "Juniya",		;Jounieh
 "Zahla",		;Zahlé
 "Jubayl",		;Byblos
 "Baabda",
 "Alayh",
 "Riyaq",
 "Ta'labaya",
 "Ad-Damur",
 "Al-Hirmil",
 "Barr Ilyas",
 "Arsal",
 "Bint Jubayl",
 "Amzit",
 "Batrun",
 "Amyun",
 "Junn Jannin",
 "Qa'wa'iyat-al-Jisr",
 "Al-Insariya",
 "Insar",
 "Zgarta",
 "Al-Fakya",
 "An-Nabi Shit",
 "'Amyar",
 "Qantara",
 "Ash-Shuwayfat",
 "Kafr Tibnit",
 "Nahr-al-Barad",
 "Aytarun",
 "Majdal 'Anjar",
 "Judaydat Marj'iyn",
 "Biskinta",
 "Al-Hiyam",
 "Shikka",
 "Al-Qusayr",
 "Shaqra",
 "'Anjar",
 "Arqa",
 "Al-Gumq"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
