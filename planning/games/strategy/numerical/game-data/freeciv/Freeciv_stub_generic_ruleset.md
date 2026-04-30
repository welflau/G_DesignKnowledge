# Freeciv(stub) · generic

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/stub/nations/generic.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, stub

## 概述
Freeciv stub规则集的generic定义

## 正文
```ruleset
[nation_generic]

name=_("People")
plural=_("?plural:People")
groups="Generic"
legend=_("This is the only nation you can select.\
")
leaders = { "name", "sex"
 "Generic", "male"
}

flag     = "aborigines"
flag_alt = "-"
style    = "Generic"

init_techs=""
init_buildings=""
init_units=""
; civilwar_nations = ""

cities =
 "Generic"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
