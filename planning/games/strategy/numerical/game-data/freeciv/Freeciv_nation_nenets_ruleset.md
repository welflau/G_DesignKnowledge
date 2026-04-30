# Freeciv(nation) · nenets

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/nenets.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的nenets定义

## 正文
```ruleset
[nation_nenets]

name=_("Nenets")
plural=_("?plural:Nenets")
groups="European"
legend=_("The Nenets are a people living in north-western Russia and\
 the most populous among the Samoyed peoples.")

leaders = {
 "name",                "sex"
 "Igor Fyodorov",       "Male"
 "Anna Nerkagi",        "Female"
 "Konstantin Pankov",   "Male"
}

flag="nenetsia"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Sami", "Mordvin"

cities =
; Cities in Nenets language
 "Nyar'yana-Mar", ; Няръянa мар, Naryan-Mar
 "Sale-Kharad", ; Сале-Харад, Salekhard
 "Neidem", ; неидэм, Nadym
 "Amderma", ; Амдерма
 "Talka-Salya", ; Талка саля, Tarko-Sale
 "Kharuto", ; Харуто, Kharuta

; Other cities in Nenets Autonomous Okrug
 "Bugrino", ; Бугрино
 "Varandey", ; Варандей
 "Indiga", ;  Индига
 "Pustozyorsk", ; Пустозёрск
 "Pylemets", ; Пылемец
 "Kharyaga", ; Харьяга

; Other cities in Yamalo-Nenets Autonomous Okrug
 "Khodovarikha", ; Ходовариха
 "Shoyna", ; Шо́йна
 "Gubkinsky", ; Губкинский
 "Labytnangi",
 "Muravlenko",
 "Novy Urengoy",
 "Noyabrsk"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
