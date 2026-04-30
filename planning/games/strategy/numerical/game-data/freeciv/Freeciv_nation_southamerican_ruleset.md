# Freeciv(nation) · southamerican

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/southamerican.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的southamerican定义

## 正文
```ruleset
[nation_southamerican]

name=_("South American")
plural=_("?plural:South Americans")
groups= "Imaginary"
legend=_("The Union of South American Nations was formed in 2008, modeled\
 after the European Union, but panamericanism has already existed since\
 the 19th century.")

leaders = {
 "name",                                "sex"
 "Francisco de Miranda",                "Male"
 "Víctor Raúl Haya de la Torre",        "Male"
 "Che Guevara",                         "Male"
}

ruler_titles = {
 "government",      "male_title",          "female_title"
 "Communism",       _("Comandante %s"),    _("Comandanta %s")
 "Despotism",       _("Caudillo %s"),      _("Caudilla %s")
 "Fundamentalism",  _("Archbishop %s"),    _("Madre %s")
}

flag="unasur"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""
conflicts_with="argentine", "bolivian", "brazilian", "chilean", "colombian",
 "ecuadorian", "guyanese", "paraguayan", "peruvian", "surinamese", "uruguayan", "venezuelan"
civilwar_nations = "argentine", "bolivian", "brazilian", "chilean", "colombian",
 "ecuadorian", "guyanese", "paraguayan", "peruvian", "surinamese", "uruguayan", "venezuelan"

cities=
; Sites of Uasur institutions
 "Quito",
 "Cochabamba",
 "Caracas"
; Subsequent cities fetched from city lists of member nations

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
