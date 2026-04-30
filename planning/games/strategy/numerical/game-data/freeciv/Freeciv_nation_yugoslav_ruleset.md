# Freeciv(nation) · yugoslav

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/yugoslav.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的yugoslav定义

## 正文
```ruleset
[nation_yugoslav]

name=_("Yugoslav")
plural=_("?plural:Yugoslavs")
groups="European"
legend=_("Yugoslavia was a state consisting of the Slavic nations of the\
 western Balkans. It was a kingdom until 1941, when it was occupied by\
 the Axis powers. After a national liberation war the communists threw\
 out the occupants and continued to rule until the 1980s. The 1990s saw\
 the bloody breakup of Yugoslavia into independent republics.")

leaders = {
 "name",                        "sex"
 "Aleksandar I Karađorđević",   "Male"
 "Pavle Karađorđević",          "Male"
 "Petar II Karađorđević",       "Male"
 "Josip Broz Tito",             "Male"
}

flag="yugoslavia"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "slovenian", "croatian", "bosnian-herzegovinian",
 "serbian", "montenegrin", "macedonian", "kosovar"
civilwar_nations = "slovenian", "croatian", "bosnian-herzegovinian",
 "serbian", "montenegrin", "macedonian"

; Cities will be fetched from above nations

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
