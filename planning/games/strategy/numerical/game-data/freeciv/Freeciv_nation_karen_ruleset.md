# Freeciv(nation) · karen

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/karen.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的karen定义

## 正文
```ruleset
[nation_karen]

name=_("Karen")
plural=_("?plural:Karens")
groups="Asian", "Ancient", "Medieval"

legend=_("Karens are a hardy mountain people who have lived on the western\
 fringes of Burmese kingdoms throughout recorded history. Their own oral\
 history suggests that they at some point migrated southwards through the\
 Gobi Desert to reach their current homeland. With the independence of\
 Burma from the United Kingdom in 1948, a heterogenous Karen armed\
 independence movement was initiated that continues to this day.")

leaders = {
 "name",                 "sex"
 "Sha Lah Phan",         "Male"
 "Win Maung",            "Male"
 "San C. Po",            "Male"
 "Ba U Gyi",             "Male"
 "Bo Mya",               "Male"
}

flag="karen"
flag_alt="-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Burmese", "Mon", "Thai"

cities =

; Kayin State
 "Hpa-An",
 "Manerplaw",
 "Mutraw", ; Hpapun
 "Dooplaya", ; Kawkareik
 "Hlaingbwe",
 "Thandang", ; Thandaung
 "Thandanggyi",
 "Myawaddy",
 "Kyeikdon",
 "Kyain Seikgyi",
 "Payathonsu",
 "Apalon",
 "Kanni",

; Kayah State
 "Loikaw",
 "Demoso",
 "Hpruso",
 "Shadaw",
 "Bawlakhe",
 "Hpasawng",
 "Mese"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
