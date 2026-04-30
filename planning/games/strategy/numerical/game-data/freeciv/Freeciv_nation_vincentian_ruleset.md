# Freeciv(nation) · vincentian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/vincentian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的vincentian定义

## 正文
```ruleset
[nation_vincentian]

name=_("Vincentian")
plural=_("?plural:Vincentians")
groups="American", "Modern"
legend=_("Saint Vincent and the Grenadines were amongst the last\
 Caribbean islands to be colonized, as local Carib Indians intermarried\
 with runaway slaves and fought off European colonizers. In the 18th\
 century the islands were contested by the French and British. In 1783\
 the French relinquished their claims. Saint Vincent and the Grenadines\
 became independent from Britain in 1979 and are currently a Commonwealth\
 realm.")

leaders = {
 "name",                        "sex"
 "Joseph Chatoyer",             "Male"
 "E.T. Joshua",                 "Male"
 "Milton Cato",                 "Male"
 "James Fitz-Allen Mitchell",   "Male"
 "Ralph Gonsalves",             "Male"
}

ruler_titles = {
 "government",      "male_title",          "female_title"
 "Fundamentalism", _("Bishop %s"),         _("?female:Bishop %s")
}

flag="svg"
flag_alt = "-"
style = "Tropical"


init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "taino", "grenadian"

cities =
 "Kingstown",
 "Georgetown",
 "Port Elizabeth (ocean)",
 "Layou",
 "Chateaubelair",
 "Barrouaillie",
 "Byera Hill",
 "Biabou",
 "Calliaqua",
 "Hamilton",
 "Dovers",
 "Cumberland",
 "Paul Over",
 "Petit Bordel",
 "Prospect",
 "Troumaca",
 "Sharps",
 "Rose Hall",
 "Colonarie",
 "Evesham",
 "Rose Bank",
 "Stubbs",
 "Ashton",
 "Clare Valley",
 "Owia",
 "Fancy",
 "Questelles",
 "Diamond Village",
 "Spring Village",
 "Lauders",
 "Vermont",
 "Mesopotamia",
 "Greiggs",
 "Sion Hill",
 "Richland Park",
 "Lodge",
 "Belmont",
 "Clifton",
 "Peruvian Vale",
 "Villa",
 "Arnos Vale"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
