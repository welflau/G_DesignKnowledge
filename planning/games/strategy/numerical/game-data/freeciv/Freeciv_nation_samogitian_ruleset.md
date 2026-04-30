# Freeciv(nation) · samogitian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/samogitian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的samogitian定义

## 正文
```ruleset
[nation_samogitian]

name=_("Samogitian")
plural=_("?plural:Samogitians")
groups="Medieval", "European"
legend=_("Samogitia - historical country near the Baltic Sea - home to the\
 last pagans in Europe (official until 1413). Today, Samogitia is a region\
 of Lithuania.")

leaders = {
 "name",        "sex"
 "Vīkints",     "Male"
 "Ringauds",    "Male"
 "Treniuota",   "Male"
 "Gedvils",     "Male"
 "Algmins",     "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("Duke %s"),         _("Duchess %s")
}

flag="samogitia"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "lithuanian"
civilwar_nations = "lithuanian", "latvian"

cities =
 "Telšē",
 "Raseinē",
 "Klaipieda",
 "Šiaulē",
 "Plongė",
 "Kretinga",
 "Varnē",
 "Reitavs",
 "Tauragie",
 "Šėlalė",
 "Kelmė",
 "Palonga",
 "Mažeikē",
 "Koršienā",
 "Akmenė",
 "Skouds",
 "Salontā",
 "Seda",
 "Kražē",
 "Trīškē",
 "Vėikšnē",
 "Muosedis"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
