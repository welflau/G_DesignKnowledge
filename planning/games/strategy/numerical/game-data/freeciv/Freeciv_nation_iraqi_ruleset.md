# Freeciv(nation) · iraqi

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/iraqi.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的iraqi定义

## 正文
```ruleset
[nation_iraqi]

name=_("Iraqi")
plural=_("?plural:Iraqis")
groups="Modern", "Asian"
legend=_("Iraq was founded after the fall of the Ottoman\
 empire. It is encompassing the ancient region of Mesopotamia at the\
 confluence of the Tigris and Euphrates rivers.")

leaders = {
 "name",                        "sex"
 "Faisal I",                    "Male"
 "Saddam Hussein",              "Male"
 "Mohammed Baqir al-Hakim",     "Male"
 "Abdul Salam Arif",            "Male"
 "Bakr Sidqi",                  "Male"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Communism",       _("Chairman %s"),       _("Chairwoman %s")
 "Fundamentalism",  _("Caliph %s"),         _("Calipha %s")
}

flag = "iraq"
flag_alt = "iraq_old"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Sumerian", "Babylonian"
civilwar_nations="Assyrian", "Kurdish", "Kuwaiti"

cities =
 "Baghdad",
 "Al-Basra",
 "Mosul",
 "An-Najaf",
 "Kirkuk",
 "Tikrit",
 "Umm Qasr",
 "Nassiriya",
 "Ar-Rutba",
 "Karbala",
 "As-Sulaymaniya",
 "Samarra",
 "Al-Kut",
 "Ar-Ramadi",
 "Arbil",
 "Kazimain",
 "Madinat as-Sadr",
 "Baiji",
 "Baquba",
 "Dahuk",
 "Al-Diwaniya",
 "Falluja",
 "Halabja",
 "Al-Hillah",
 "Iskandariya",
 "Muqdadiya",
 "Osiraq",
 "Samawa",
 "Tadji"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
