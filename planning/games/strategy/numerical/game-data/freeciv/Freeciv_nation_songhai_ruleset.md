# Freeciv(nation) · songhai

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/songhai.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的songhai定义

## 正文
```ruleset
[nation_songhai]

translation_domain="freeciv"

name=_("Songhai")
plural=_("?plural:Songhai")
groups="Medieval", "African", "Core"
legend=_("The Songhai people established a state in the 11th century CE\
 centered on the city of Gao. Following the decline of the Mali empire\
 a few hundred years later, the Songhai established an empire of their own\
 which eventually grew to become one of the largest in the history of\
 Africa. The rulers of Songhai became known for their wealth as well as\
 their devotion to the Muslim faith.")

leaders = {
 "name",                        "sex"
 "Askia Ishaq I",               "Male"
 "Askia Daoud",                 "Male"
 "Askia Mohammad Benkan",       "Male"
 "Askia Mohammad I",            "Male"
 "Sonni Ali",                   "Male"
 "Sunni Silman Dandi",          "Male"
}
ruler_titles = {
 "government",      "male_title",      "female_title"
 "Fundamentalism",  _("Caliph %s"),    _("Calipha %s")
 "Monarchy",        _("Mansa %s"),     _("?female:Mansa %s")
}

flag="songhai"
flag_alt="-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
conflicts_with = "Malian", "Nigerien"
civilwar_nations = "Nigerien", "Burkinabe"

cities =
 "Gao",
 "Jenne",
 "Timbuktu",
 "Kumbi Saleh",
 "Taghaza",
 "Kukiya",
 "Tekedda",
 "Agadez",
 "Tadmekket",
 "Walata",
 "Kano",
 "Awdaghost",
 "Niani",
 "Kangaba",
 "Tondibi",
 "Tabelbala",
 "Agades",
 "Katsina",
 "Taudeni",
 "Bandiagara",
 "Karabara",
 "Ras el Ma",
 "Hombori"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
