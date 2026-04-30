# Freeciv(nation) · iberian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/iberian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的iberian定义

## 正文
```ruleset
[nation_iberian]

name=_("Iberian")
plural=_("?plural:Iberians")
groups="Ancient", "European"
legend=_("The Iberians were non-Indo-European inhabitants of the\
 ancient Iberian Peninsula. Very little is known about their history.\
 They were subjugated by Rome in the last centuries BCE.")

leaders = {
 "name",        "sex"
 "Budar",       "Male"
 "Busadines",   "Male"
 "Himilce",     "Female"
 "Indibil",     "Male"
 "Korbis",      "Male"
 "Korribilo",   "Male"
 "Mandonio",    "Male"
}

flag="iberian"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""
conflicts_with = "spanish", "portuguese", "castilian", "catalan", "aragonese"
civilwar_nations = "basque", "etruscan", "celtiberian" ;lustianian tartessian

cities =
 "Kastulo",
 "Gadir",
 "Ilipla",
 "Asido",
 "Orippo",
 "Asta",
 "Myrtilis",
 "Kaetobriga",
 "Balsa",
 "Balleia",
 "Emporion",
 "Karmo",
 "Kinniana",
 "Dekiana",
 "Ilipa",
 "Ilturir",
 "Astigis",
 "Konistorgis",
 "Korduba",
 "Ipolka",
 "Odisseia",
 "Aurgi",
 "Hispalis",
 "Abra",
 "Akra Leuke",
 "Bora",
 "Tuki",
 "Baesuri",
 "Baria",
 "Akinipo",
 "Pesula",
 "Ebusos",
 "Urso",
 "Rhoda",
 "Abdera",
 "Iptuki",
 "Ostippo",
 "Junkaria",
 "Onuba",
 "Karisa",
 "Salalia",
 "Ossonoba",
 "Indika",
 "Kallentum",
 "Sexs"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
