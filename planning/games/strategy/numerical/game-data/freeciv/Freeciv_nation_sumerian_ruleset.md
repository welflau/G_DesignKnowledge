# Freeciv(nation) · sumerian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/sumerian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的sumerian定义

## 正文
```ruleset
[nation_sumerian]

translation_domain="freeciv"

name=_("Sumerian")
plural=_("?plural:Sumerians")
groups="Ancient", "Asian", "Core"
legend=_("Sumer controlled southern Mesopotamia until the rise of\
 Babylonia. Tablets of Sumerian writing some 5500 years old have been\
 found, pre-dating every other writing in history.")

leaders = {
 "name",                "sex"
 "Shulgi",              "Male"
 "Gilgamesh",           "Male"
 "Ur-Nanshe",           "Male" ; a.k.a. Ur-Nina
 "Lugal-Za-Gesi",       "Male"
 "En-Mer-Kar",          "Male"
 "Urukagina",           "Male"
 "Etana",               "Male"
 "Ur-Nammu",            "Male"
 "Ibbi-Sin",            "Male"
 "Nin-Kasalsi",         "Female"
}

ruler_titles = {
 "government", "male_title",    "female_title"
 "Anarchy",    _("Usurper %s"), _("?female:Usurper %s")
 "Monarchy",   _("%s Lugal"),   _("?female:%s Lugal")
}

flag = "sumeria"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="assyrian", "egyptian", "babylonian"

cities =
 "Unug", ; Uruk
 "Eridug", ; Eridu
 "Urim", ; Ur
 "Sirpurla", ; Lagash
 "Nibru", ; Nippur
 "Umma",
 "Larsa",
 "Kish",
 "Adab",
 "Hit",
 "Agade", ; Akkad
 "Borsippa",
 "Isin",
 "Shuruppak",
 "Ngirsu", ; Girsu
 "Bad-tibira",
 "Zimbir", ; Sippar
 "Gudua", ; Kutha
 "Dilbat",
 "Marda", ; Marad
 "Der",
 "Kisurra",
 "Zabala",
 "Kisiga", ; Kuara
 "Kes",
 "Hamazi",
 "Eshnunna",
 "Akshak",
 "Mari",
 "Kesh"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
