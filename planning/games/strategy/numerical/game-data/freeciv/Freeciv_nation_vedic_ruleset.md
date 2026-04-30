# Freeciv(nation) · vedic

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/vedic.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的vedic定义

## 正文
```ruleset
[nation_vedic]

name=_("Vedic")
plural=_("?plural:Vedics")
groups="Ancient", "Asian"
legend=_("The cradle of Ancient Indian civilization lay in the Indus river\
 valley in modern-day Pakistan.")

leaders = {
 "name",                "sex"
 "Ashoka",              "Male"
 "Chandragupta Maurya", "Male"
 "Mahapadma Nanda",     "Male"
 "Janak",               "Male"
 "Jarasandha",          "Male"
 "Gargi",               "Female"
 "Brihadratha",         "Male"
 "Ikshvaku",            "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("Raja %s"),      _("Rani %s")
 "Fundamentalism",  _("Guru %s"),      _("?female:Guru %s")
 "Monarchy",        _("Maharaja %s"),  _("Maharani %s")
 "Republic",        _("Mahatma %s"),   _("?female:Mahatma %s")
}

flag="vedic"
flag_alt="-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Indian", "Pakistani"
civilwar_nations="Gupta", "Sikh", "Kashmiri"

cities =
 "Varanasi",
 "Savatthi",
 "Champa",
 "Rajagriha",
 "Mithila",
 "Chandrakanta",
 "Sukti",
 "Kausambi",
 "Indraprastha",
 "Adhichhatra",
 "Viratanagara",
 "Madhura",
 "Potana",
 "Mahissati",
 "Takshasila",
 "Rajapura",
 "Ayodhya",
 "Magadhapura",
 "Vaishali",
 "Kampilya",
 "Ujjaini",
 "Saketa",
 "Pataliputra"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
