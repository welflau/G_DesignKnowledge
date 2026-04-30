# Freeciv(nation) · estonian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/estonian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的estonian定义

## 正文
```ruleset
[nation_estonian]

name=_("Estonian")
plural=_("?plural:Estonians")
groups="Modern", "European"
legend=_("Estonia is a small country on the south shore of the eastern\
 Baltic Sea.  Its people and language are closely related to those of\
 Finland.")

leaders = {
 "name",                        "sex"
 "Kalevipoeg",                  "Male"
 "Lembitu",                     "Male"
 "Carl Robert Jakobson",        "Male"
 "Konstantin Päts",             "Male"
 "Lennart Meri",                "Male"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Despotism",       _("Protector %s"),   _("?female:Protector %s")
 "Fundamentalism",  _("Elder %s"),       _("?female:Elder %s")
}

flag="estonia"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="finnish", "latvian"
; Removed "danish", "dutch": No relation?

cities =
  "Tallinn", "Tartu", "Narva", "Kohtla-Järve", "Pärnu",
  "Viljandi", "Rakvere", "Valga", "Võru", "Sillamäe",
  "Kuressaare", "Haapsalu", "Kiviõli", "Tapa", "Paide",
  "Maardu", "Paldiski", "Türi", "Keila", "Elva",
  "Kunda", "Põltsamaa", "Sindi", "Kärdla", "Tõrva",
  "Otepää", "Kilingi-Nõmme", "Mustvee", "Antsla", "Mõisaküla",
  "Suure-Jaani", "Kallaste", "Mustla"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
