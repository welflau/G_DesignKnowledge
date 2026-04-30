# Freeciv(stub) · barbarian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/stub/nations/barbarian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, stub

## 概述
Freeciv stub规则集的barbarian定义

## 正文
```ruleset
[nation_barbarian]

name=_("Barbarian")
plural=_("?plural:Barbarians")
legend=_("Since the dawn of civilization, barbarians have been a threat to\
 cultured peoples everywhere.")
leaders = { "name", "sex"
 "Barbarian", "male"
}

flag     = "barbarian"
flag_alt = "-"
style    = "Generic"

init_techs=""
init_buildings=""
init_units=""

cities = "Barbaricum"

is_playable = FALSE
barbarian_type = "LandAndSea"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
