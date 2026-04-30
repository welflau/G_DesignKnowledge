# Freeciv(nation) · gupta

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/gupta.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的gupta定义

## 正文
```ruleset
[nation_gupta]

name=_("Gupta")
plural=_("?plural:Gupta")
groups="Asian", "Ancient"

legend=_("The Gupta Empire was one of the great classical empires. It\
 ruled northern India from around 240 to 550 CE.")

leaders = {
 "name",                "sex"
 "Chandra Gupta I",     "Male"
 "Sumudra Gupta",       "Male"
 "Kumara Gupta",        "Male"
 "Skanda Gupta",        "Male"
 "Chandra Gupta II",    "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Despotism",       _("Raja %s"),            _("Rani %s")
 "Monarchy",        _("Maharaja %s"),        _("Maharani %s")
}

flag         = "gupta"
flag_alt     = "-"
style        = "Babylonian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="indian", "bengali"

cities =
 "Pataliputra",
 "Ujjain",
 "Ayodhya",
 "Mathura",
 "Padmava",
 "Licron",
 "Vengi",
 "Sanchi",
 "Girnar",
 "Mandasor",
 "Rajagriha",
 "Bodh Gaya",
 "Kasi",
 "Sarnath",
 "Bharut",
 "Kausaubi",
 "Prayaga",
 "Sravasti",
 "Indraprastra",
 "Hastinapura",
 "Kurukshatra",
 "Broach",
 "Tmralipti",
 "Thanesar",
 "Gwalior",
 "Nalanda"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
