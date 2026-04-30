# Freeciv(nation) · moldovan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/moldovan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的moldovan定义

## 正文
```ruleset
[nation_moldovan]

name=_("Moldovan")
plural=_("?plural:Moldovans")
groups="Modern", "European"
legend=_("Moldova was conquered by the Ottomans in the 16th century.\
 Then in 1812 Moldova became part of the Russian Empire.\
 From 1918 Moldova was part of Romania until inclusion\
 in the Soviet Union in 1940. The modern Republic of Moldova\
 gained independence from the Soviet Union in 1991.")

leaders = {
 "name",                        "sex"
 "Dragoş",                      "Male"
 "Ştefan cel Mare şi Sfânt",    "Male"
 "Vasile Lupu",                 "Male"
 "Dimitrie Cantemir",           "Male"
 "Alexandru Ioan Cuza",         "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("Prince %s"),      _("Princess %s")
 "Fundamentalism",  _("Patriarch %s"),   _("Matriarch %s")
}

flag="moldova"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "romanian", "transnistrian", "turkish"

cities =
  "Chişinau",
  "Bălţi",
  "Cahul",
  "Comrat",
  "Hinceşti",
  "Căuşeni",
  "Ungheni",
  "Soroca",
  "Orhei",
  "Edineţ",
  "Lipcani",
  "Briceni",
  "Ocniţa",
  "Cupcini",
  "Donduşeni",
  "Timova",
  "Rişcani",
  "Drochia",
  "Costeşti",
  "Floreşti",
  "Chubdeşti",
  "Soldăneşti",
  "Balatina",
  "Glodeni",
  "Singerei",
  "Rezina",
  "Teleneşti",
  "Sculeni",
  "Corneşti",
  "Călăraşi",
  "Criuleni",
  "Nispoleni",
  "Străşeni",
  "Ialoveni",
  "Singera",
  "Cărpineni",
  "Lăpuşna",
  "Anenii Noi",
  "Leova",
  "Cimişlia",
  "Cainari",
  "Olăneşti",
  "Iargara",
  "Basarabeasca",
  "Cantemir",
  "Congaz",
  "Ceadîr-Lunga",
  "Taraclia",
  "Vulcăneşti"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
