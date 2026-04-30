# Freeciv(nation) · afghani

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/afghani.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的afghani定义

## 正文
```ruleset
[nation_afghani]

name=_("Afghani")
plural=_("?plural:Afghanis")
groups="Early Modern", "Modern", "Asian"
legend=_("Afghanistan, often called the crossroads of Central Asia, has had\
 a very turbulent history. Through the ages, the country has been occupied\
 by many forces including the Persian Empire, Genghis Khan and Alexander the\
 Great. The Afghanistan nation-state as it is known today came into existence\
 in 1746 when Ahmad Shah founded the Durrani Empire.")

leaders = {
 "name",                "sex"
 "Kanishka",            "Male"
 "Mahmud Ghaznawi",     "Male"
 "Ahmad Shah Durrani",  "Male"
 "Zahir Shah",          "Male"
 "Daoud Khan",          "Male"
}

ruler_titles = {
 "government",      "male_title",          "female_title"
 "Monarchy",        _("Emir %s"),          _("Emira %s")
 "Communism",       _("General Secretary %s"), _("?female:General Secretary %s")
 "Fundamentalism",  _("Mullah %s"),        _("?female:Mullah %s")
}

flag="afghanistan"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Iranian", "Pakistani", "Pashtun"

; City list based on data from this page:
; http://de.wikipedia.org/wiki/Liste_der_Städte_in_Afghanistan
cities =
 "Kabul",
 "Kandahar",
 "Mazar-e Sharif",
 "Herat",
 "Kunduz",
 "Jalalabad",
 "Ghazni",
 "Merv",
 "Baghlan",
 "Gardez",
 "Bamiyan",
 "Maimana",
 "Balkh",
 "Hanabad",
 "Kholm",
 "Taloqan",
 "Pol-e Khomri",
 "Sheberghan",
 "Charikar",
 "Qal'eh-ye Now",
 "Sar-e Pol",
 "Aqchah",
 "Ghurian",
 "Paghman",
 "Asadabad",
 "Aybak",
 "Lashkar Gah",
 "Gereshk",
 "Farah",
 "Faizabad",
 "Tash Gozar",
 "Zaranj",
 "Chaghcharan",
 "Baghrami",
 "Peshawar",
 "Andkhui",
 "Deshu",
 "Kang",
 "Ab Gach",
 "Qalat",
 "Samangan",
 "Mahmud-e Raq",
 "Maydanshahr"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
