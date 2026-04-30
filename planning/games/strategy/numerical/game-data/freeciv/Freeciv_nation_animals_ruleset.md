# Freeciv(nation) · animals

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/animals.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的animals定义

## 正文
```ruleset
[nation_animals]

translation_domain="freeciv"

name=_("Animal Kingdom")
plural=_("?plural:Animals")
groups="Core", "Barbarian"
legend=_("Before civilization claimed the lands, ancient man had to \
survive the wilderness with all kinds of dangerous animals.")

leaders = {
 "name",        "sex"
 "Lion",        "Female"
 "Orca",        "Male"
}

flag     = "animals"
flag_alt = "barbarian"
style    = "European"

init_techs=""
init_buildings=""
init_units=""

cities = "Wilderness"

is_playable = FALSE
barbarian_type = "Animal"

; nothing more needed for barbarians

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
