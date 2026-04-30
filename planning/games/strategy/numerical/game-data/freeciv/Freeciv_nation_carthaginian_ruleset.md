# Freeciv(nation) · carthaginian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/carthaginian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的carthaginian定义

## 正文
```ruleset
[nation_carthaginian]

translation_domain="freeciv"

name=_("Carthaginian")
plural=_("?plural:Carthaginians")
groups="Ancient", "African", "Core"
; Carthage being a successor-state of the Phoenician empire
conflicts_with="phoenician"
legend=_("The Carthaginians, descendants of Phoenician traders,\
 ran a naval empire in the Mediterranean from the 5th to 2nd centuries\
 BCE. Carthage was destroyed by Rome in 146 BCE.")

leaders = {
 "name",                "sex"
 "Hannibal Barca",      "Male"
 "Hasdrubal Barca",     "Male"
 "Hamilcar Barca",      "Male"
 "Dido",                "Female"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Anarchy",         _("Usurper %s"),     _("?female:Usurper %s")
 "Democracy",       _("Judge %s"),       _("?female:Judge %s")
}

flag="cartago"
flag_alt = "tunisia"	; Used previously
style = "Classical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="phoenician", "sicilian", "iberian"

;Ancient cities from Africa and south Spain,
;some are later roman colonies and not carthaginian towns

cities =
  "Carthago", "Leptis Magna", "Cirta", "Hadrumetum", "Aspis",
  "Charax", "Oea", "Sabrata", "Utica", "Saldae", "Cartenna",
  "Siga", "Rusaddir", "Tingis", "Gades", "Malaca", "Mastia",
  "Thapsus", "Capsa", "Thugga", "Thevesta", "Madaura", "Sitifis",
  "Githis", "Uthina", "Thamugaddi", "Lambaesis"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
