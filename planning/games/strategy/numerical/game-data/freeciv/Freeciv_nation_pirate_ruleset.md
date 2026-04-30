# Freeciv(nation) · pirate

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/pirate.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的pirate定义

## 正文
```ruleset
[nation_pirate]

translation_domain="freeciv"

name=_("Pirate")
plural=_("?plural:Pirates")
groups="Core", "Barbarian"
legend=_("As long as honest men have sailed the seas, pirates have been a\
 scourge of them and of all coastal dwelling peoples.")

leaders = {
 "name",                        "sex"
 "Anne Bonny",                  "Female"
 "Calico Jack",                 "Male"
 "Roberto Cofresí",             "Male"
 "Blackbeard",                  "Male"
 "Henry Morgan",                "Male"
 "François l'Olonais",          "Male"
 "Bartolomeu Português",        "Male"
 "Ching Shih",                  "Female"
}

flag="pirate"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

; Various pirate havens
cities =
 "New Providence",
 "Port Royal", 
 "Tortuga"

is_playable = FALSE
barbarian_type = "Sea"

; nothing more needed for barbarians

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
