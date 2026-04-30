# Freeciv(nation) · thracian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/thracian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的thracian定义

## 正文
```ruleset
[nation_thracian]

name=_("Thracian")
plural=_("?plural:Thracians")
groups="Ancient", "European"

legend=_("The second most numerous people in the ancient western world.")

leaders = {
 "name",        "sex"
 "Thiras",      "Male"
 "Burebista",   "Male"
 "Decebalus",   "Male"
 "Seuthes",     "Male"
 "Spartacus",   "Male"
}

; A dragon was depicted on the standard of the Thracians.
flag="thrace"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="bosporan", "illyrian", "macedon", "dacian"

cities =
 "Uscudama",
 "Sarmizegetusa",
 "Perperikon",
 "Oescus",
 "Byzantion",
 "Agathapara",
 "Authiparu",
 "Bazopara",
 "Bedizos",
 "Belaidipara",
 "Bendipara",
 "Beodizos",
 "Beripara",
 "Bessapara",
 "Bospara",
 "Breierophara",
 "Brentopara",
 "Briparon",
 "Burtudizos",
 "Chesdupara",
 "Dardapara",
 "Dodoparos",
 "Drusipara",
 "Gelupara",
 "Iamphorynna",
 "Isgipera",
 "Ismara",
 "Isgipera",
 "Keirpara",
 "Kistidizos",
 "Krasalopara",
 "Longinopara",
 "Maskiobria",
 "Mesambria",
 "Mutzipara",
 "Orudisza",
 "Ostudizos",
 "Poltymbria",
 "Priskupera",
 "Skedabria",
 "Spinopara",
 "Stratopara",
 "Subzupara",
 "Tranupara",
 "Tyrodiza"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
