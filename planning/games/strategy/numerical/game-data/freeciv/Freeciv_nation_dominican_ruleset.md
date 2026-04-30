# Freeciv(nation) · dominican

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/dominican.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的dominican定义

## 正文
```ruleset
[nation_dominican]

name=_("Dominican")
plural=_("?plural:Dominicans")
groups="Modern", "American"
legend=_("The island of Dominica was first sighted by Europeans, including\
 Christopher Columbus, in 1493. Legend has it that the island was named so\
 since the day of its first sighting was a Sunday. Officially the\
 \"Commonwealth of Dominica\", the country should not be confused with the\
 Dominican Republic, another Caribbean nation.")

leaders = {
 "name",                "sex"
 "Roosevelt Skerrit",   "Male"
 "Pierre Charles",      "Male"
 "Rosie Douglas",       "Male"
 "Jennes Armour",       "Male"
}

ruler_titles = {
 "government",     "male_title",           "female_title"
 "Fundamentalism", _("Bishop %s"),         _("Mother Superior %s")
}

flag="dominica"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="cuban"

cities =
 "Roseau",
 "Portsmouth (ocean)",
 "Berekua",
 "Marigot",
 "Grand Bay (ocean)",
 "Atkinson",
 "Mahaut",
 "Canefield",
 "Saint Joseph",
 "Wesley",
 "Coulihaut",
 "Pointe Michel",
 "Barroui",
 "Salisbury",
 "Castle Bruce",
 "La Plaine",
 "Massacre",
 "Woodford Hill (hills)",
 "Calibishie",
 "Soufrière",
 "Rosalie",
 "Pont Cassé"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
