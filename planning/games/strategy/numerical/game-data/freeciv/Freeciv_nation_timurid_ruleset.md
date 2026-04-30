# Freeciv(nation) · timurid

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/timurid.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的timurid定义

## 正文
```ruleset
[nation_timurid]

name=_("Timurid")
plural=_("?plural:Timurids")
groups="Medieval", "Asian"
legend=_("Timur was a military genius who claimed lineage from Chinggis\
 Khan and from his capital in Samarkand conquered all of Central Asia as\
 well as parts of the Middle East and India. The court culture of Timurid\
 Empire was heavily Persianized, while the imperial administration and\
 military organization displayed influences from the Timurid ruling elite's\
 Mongolian and Turkic origins.")

leaders = {
 "name",             "sex"
 "Husayn Bayqarah",  "Male"
 "Abu Sa'id",        "Male"
 "Ulugh Beg",        "Male"
 "Goharshad",        "Female"
 "Shah Rukh",        "Male"
 "Timur",            "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("%s Khan"),      _("%s Khatan")
 "Monarchy",        _("Emir %s"),      _("Emira %s")
 "Fundamentalism",  _("Caliph %s"),    _("Calipha %s")
}

flag="timur"
flag_alt="-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Uzbek", "Tajik", "Iranian", "Afghani", "Mughal"

cities =
 "Samarkand",
 "Herat",
 "Bokhara",
 "Tashkent",
 "Balkh",
 "Otrar",
 "Khojent",
 "Kharesm",
 "Kish",
 "Balkh",
 "Ghazni",
 "Merv",
 "Kabul",
 "Kandahar",
 "Nishapur",
 "Sebzewar",
 "Rai",
 "Ispahan",
 "Shiraz",
 "Alamut",
 "Bagdad",
 "Basra",
 "Ardabil",
 "Tabriz",
 "Van"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
