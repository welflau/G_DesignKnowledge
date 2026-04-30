# Freeciv(nation) · jaffna

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/jaffna.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的jaffna定义

## 正文
```ruleset
[nation_jaffna]

name=_("Jaffna")
plural=_("?plural:Jaffnas")
groups="Asian", "Early Modern", "Medieval"

legend=_("The Jaffna Kingdom was a medieval Tamil kingdom based in the\
 north of Sri Lanka. It was a successful southern rival to the Chola\
 Empire on the Indian mainland.")

leaders = {
 "name",                 "sex"
 "Cankili I",               "Male"
 "Singai Pararasasegaram",  "Male"
 "Martanda Cinkaiariyan",   "Male"
 "Varodaya Cinkaiariyan",   "Male"
 "Kulingai Cakravarti",     "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("Raja %s"),      _("Rani %s")
 "Monarchy",        _("Maharaja %s"),  _("Maharani %s")
}

flag="jaffna"
flag_alt="-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Lankese"
civilwar_nations="Chola", "Sinhalese"

cities =

; Jaffar District
 "Nallur",
 "Kopay",
 "Sandilipay",
 "Chavakacheri",
 "Uduvil",
 "Karaveddy",
 "Paruthithurai", ; Point Pedro
 "Chankanai",
 "Tellippalai",
 "Maruthankerney",
 "Kayts",
 "Velanai",
 "Karainagar",
 "Neduntheevu",

; Mannar District
 "Mannar",
 "Adampan",
 "Nanattan",
 "Madhu",
 "Chilawathurai",

; Kilinochchi District
 "Kilinochchi",
 "Kandawalai",
 "Pooneryn",
 "Pallai",

; Mullaitivu District
 "Mullaitivu",
 "Puthukkudiyiruppu",
 "Oddusuddan",
 "Thunukkai",
 "Pandiyankulam",

; Vavuniya District
 "Vavuniya",
 "Cheddikulam",
 "Nedunkeni",
 "Madukandai"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
