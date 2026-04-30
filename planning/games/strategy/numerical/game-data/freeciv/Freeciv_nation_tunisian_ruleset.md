# Freeciv(nation) · tunisian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/tunisian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的tunisian定义

## 正文
```ruleset
[nation_tunisian]

name=_("Tunisian")
plural=_("?plural:Tunisians")
groups="Modern", "African"
legend=_("The Phoenicians founded Carthage in the area where Tunisia is\
 today. Carthage later became a major power in the Mediterranean region\
 until it was defeated by the Romans in 146 BCE. Later the Arab Muslim\
 conquest in the 7th century led to migration from the Arab and Ottoman\
 countries. But there were also a lot of Jews and Spanish Moors who moved\
 there at the end of the 16th century. Tunisia became mostly autonomous from\
 the Ottoman empire in 1861. But in 1881 Tunisia was invaded by the French\
 and was made a French protectorate. The country became independent in\
 1956.")

leaders = {
 "name",                        "sex"
 "Hussein bin Ali Agha",        "Male"
 "Khair ad-Din",                "Male"
 "Mustapha Khaznadar",          "Male"
 "Muhammad al-Munsif",          "Male"
 "Habib Bourguiba",             "Male"
 "Hedi Amara Nouira",           "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("%s Bey"),       _("?female:%s Bey")
 "Fundamentalism",  _("Caliph %s"),    _("Calipha %s")
}

flag="tunisia"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Carthaginian"
civilwar_nations="Algerian", "Libyan", "Amazigh"

cities =
  "Tunis",
  "Gabes",
  "Bizerte",
  "Susah",
  "Sfax",
  "El Kef",
  "Nabaul",
  "Kesserine",
  "Gafsa",
  "Bajah",
  "Tozeur",
  "Manzil Bu Raqaybah",
  "Medenine",
  "Tataouine",
  "Zarzis",
  "Madanin",
  "Duz",
  "Tawzar",
  "Al Munastir",
  "Al Mahdiyah"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
