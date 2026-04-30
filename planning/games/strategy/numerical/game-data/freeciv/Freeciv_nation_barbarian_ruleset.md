# Freeciv(nation) · barbarian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/barbarian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的barbarian定义

## 正文
```ruleset
[nation_barbarian]

translation_domain="freeciv"

name=_("Barbarian")
plural=_("?plural:Barbarians")
groups="Core", "Barbarian"
legend=_("Since the dawn of civilization, barbarians have been a threat to\
 cultured peoples everywhere.")

leaders = {
 "name",        "sex"
 "Genseric",    "Male"
 "Alaric",      "Male"
 "Theodoric",   "Male"
 "Stilicho",    "Male"
 "Attila",      "Male"
 "Boudica",     "Female"
}

flag="barbarian"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

cities = "Barbaricum"

is_playable = FALSE
barbarian_type = "Land"

; nothing more needed for barbarians

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
