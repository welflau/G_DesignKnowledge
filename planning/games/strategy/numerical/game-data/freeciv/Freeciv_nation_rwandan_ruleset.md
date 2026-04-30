# Freeciv(nation) · rwandan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/rwandan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的rwandan定义

## 正文
```ruleset
[nation_rwandan]

name=_("Rwandan")
plural=_("?plural:Rwandans")
groups="Modern", "African"
legend=_("Rwanda is a hilly and very fertile country in the Great Lakes\
 region of eastern Africa. It supports the densest population of\
 the continent.")

leaders = {
 "name",                "sex"
 "Juvénal Habyarimana", "Male"
 "Grégoire Kayibanda",  "Male"
 "Kigeli V",            "Male"
 "Mutara III",          "Male"
 "Yuhi IV",             "Male"
}

flag="rwanda"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "burundian", "congolese"

; http://de.wikipedia.org/wiki/Liste_der_Städte_in_Ruanda
cities =
 "Kigali",
 "Butare",
 "Gitarama",
 "Ruhengeri",
 "Gisenyi",
 "Byumba",
 "Cyangugu",
 "Nyanza",
 "Kabuga",
 "Ruhango",
 "Rwamagana",
 "Kibuye",
 "Kibungo",
 "Gikongoro",
 "Umutara"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
