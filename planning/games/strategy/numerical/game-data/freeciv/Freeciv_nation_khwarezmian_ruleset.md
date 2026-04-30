# Freeciv(nation) · khwarezmian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/khwarezmian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的khwarezmian定义

## 正文
```ruleset
[nation_khwarezmian]

name=_("Khwarezmian")
plural=_("?plural:Khwarezmians")
groups="Asian", "Ancient", "Medieval"

legend=_("Known by the Greeks as Chorasmia, Khwarezm was an urbanized,\
 centralized, and militarized state south of the Aral sea in Central Asia,\
 controlling portions of the Silk Road. It was loosely controlled as a\
 satrapy under the Achaemenid and Sassanid Persian dynasties and was the\
 mythic homeland of Zarathustra, the founder of Zoroastrianism. Following\
 the introduction of Islam, Khwarezm tended to be divided into two\
 separate kingdoms, but was united under the Turkic Anushtiginid dynasty,\
 which lasted from 1097 until Chinggis Khan conquered it in 1231.")

leaders = {
 "name",                "sex"
 "Vishtaspa",           "Male" ; Hystaspes
 "Artav",               "Male" ; Artabanos
 "Nustekin Gharcha",    "Male" ; Anushtigin Gharchai
 "Mamun I",             "Male"
 "Atsiz",               "Male"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Despotism",       _("Satrap %s"),      _("?female:Satrap %s")
 "Monarchy",        _("%s Shah"),        _("%s Shahbanu")
}

flag         = "khwarezm"
flag_alt     = "-"
style        = "Babylonian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Persian", "Tocharian"

cities =
 "Gurganj",
 "Kath",
 "Samarkand",
 "Chach",
 "Sarazm",
 "Balkh",
 "Khiveh",
 "Bukhara",
 "Khalchayan",
 "Otrar",
 "Dzanbas-Kala",
 "Khujand",
 "Shahrisadz",
 "Kesh",
 "Chirik-Rabat",
 "Merv",
 "Giaur-Kala",
 "Hujeli",
 "Khavakend",
 "Zaman Baba",
 "Sanjan",
 "Zeravshan",
 "Usrushana",
 "Toprak-Kala",
 "Nakhshab",
 "Karmana",
 "Koy-Krylgan-Kala",
 "Tagisken",
 "Nukus",
 "Talas"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
