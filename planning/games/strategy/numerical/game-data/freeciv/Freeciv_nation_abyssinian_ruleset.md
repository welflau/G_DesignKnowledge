# Freeciv(nation) · abyssinian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/abyssinian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的abyssinian定义

## 正文
```ruleset
[nation_abyssinian]

name=_("Abyssinian")
plural=_("?plural:Abyssinians")
groups="Ancient", "Medieval", "Early Modern", "African"
legend=_("Abyssinians - also known as Habesha or Ethiopians - are a\
 Semitic people who ruled historical states in the Horn of Africa, the\
 most prominent being the Aksumite Kingdom and the Ethiopian Empire.")

leaders = {
 "name",                "sex"
 "Ezana",               "Male"
 "Yekuno Amlak",        "Male"
 "Lalibela",            "Male"
 "Eleni",               "Female"
 "Dawit II",            "Male"
 "Menelik II",          "Male"
 "Haile Selassie",      "Male"
}

ruler_titles = {
 "government",      "male_title",       "female_title"
 "Fundamentalism",  _("Patriarch %s"),  _("Matriarch %s")
 "Monarchy",        _("Emperor %s"),    _("Empress %s")
}

flag="ethiopia_old"
flag_alt="-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Ethiopian", "Eritrean", "Nubian"
conflicts_with="Ethiopian", "Eritrean"

cities =
 "Yeha",
 "Aksum",
 "Wukro",
 "Matara",
 "Adulis",
 "Qohaito",
 "Hawulti",
 "Mendefera",
 "Zula",
 "Dungur",
 "Lalibela",
 "Gondar",
 "Debarwa",
 "Mek'ele",
 "Adigrat",
 "Gefegef",
 "Tiya",
 "Debre Berhan",
 "Magdala"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
