# Freeciv(nation) · sinhalese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/sinhalese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的sinhalese定义

## 正文
```ruleset
[nation_sinhalese]

name=_("Sinhalese")
plural=_("?plural:Sinhalese")
groups="Asian", "Ancient", "Medieval"

legend=_("The Sinhalese people of Sri Lanka trace their ancestry to\
 the semi-legendary Prince Vijaya who settled the island of Sri Lanka\
 together with 700 followers in 543 BCE.")

leaders = {
 "name",                 "sex"
 "Parakramabahu VI",     "Male"
 "Parakramabahu II",     "Male"
 "Vijayabahu I",         "Male"
 "Anula",                "Female"
 "Dutthagamani",         "Male"
 "Devanampiya Tissa",    "Male"
 "Kuveni",               "Female"
 "Vijaya",               "Male"
}

ruler_titles = {
 "government",   "male_title",             "female_title"
 "Despotism",    _("Prince %s"),           _("Princess %s")
}

flag="sinhalese"
flag_alt="-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Lankese"
civilwar_nations="Chola", "Gupta"

cities =
 "Anuradhapura",
 "Jambukola",
 "Mathoddam",
 "Mahatittha",
 "Urkavalthurai",
 "Gokanna",
 "Katharagama",
 "Polonnaruwa",
 "Dambadeniya",
 "Yapahuwa",
 "Kurunegala",
 "Gampola",
 "Dedigama",
 "Raigama",
 "Kotte",
 "Kelaniya",
 "Sitawaka",
 "Senkadagalapura",
 "Balane",
 "Gannoruwa",
 "Mudda Kalapuwa",
 "Thrikunamalaya",
 "Kalutara",
 "Puttalam",
 "Kalpitiya"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
