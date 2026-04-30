# Freeciv(nation) · southsudanese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/southsudanese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的southsudanese定义

## 正文
```ruleset
[nation_southsudanese]

name=_("South Sudanese")
plural=_("?plural:South Sudanese")
groups="Modern", "African"
legend=_("A long civil war pitted Southern Sudan, inhabited mostly by black\
 Africans and predominantly Animist and Christian, against the Muslim and\
 Arab North. The war left two million dead and many more displaced until a\
 ceasefire was signed in 2005. Southern Sudan achieved full independence\
 in 2011.")

leaders = {
 "name",                       "sex"
 "John Garang",                "Male"
 "Dominic Dim Deng",           "Male"
 "Rebecca Nyandeng De Mabior", "Female"
 "Salva Kiir Mayardit",        "Male"
}

flag="southern_sudan"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="sudanese", "ugandan"

cities =
 "Juba",
 "Wau",
 "Malakal",
 "Bor",
 "Nimule",
 "Rumbek",
 "Yambio",
 "Torit",
 "Aweil",
 "Kapoeta",
 "Kuajok",
 "Warrap",
 "Yei",
 "Kodok",
 "Dimo",
 "Rokon",
 "Raga",
 "Kajo Keji",
 "Mapel",
 "Mbeli",
 "Bussery",
 "Kangi",
 "Busilia",
 "Ujugo"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
