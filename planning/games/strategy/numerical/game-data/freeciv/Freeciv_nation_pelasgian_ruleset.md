# Freeciv(nation) · pelasgian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/pelasgian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的pelasgian定义

## 正文
```ruleset
[nation_pelasgian]

name=_("Pelasgian")
plural=_("?plural:Pelasgians")
groups="Ancient", "European"
legend=_("Pelasgians or Pelasgoi were an ancient pre-Greek people of Greece.\
 Much is still unknown about them, but it is probable they were of\
 pre-Indo-European origin.")
leaders = {
 "name",                "sex"
 "Pelasgos",            "Male"
 "Minyas",              "Male"
 "Athamas",             "Male"
 "Ogyges",              "Male"
 "Phoroneus",           "Male"
 "Kekrops",             "Male"
}
flag="pelasgian"
flag_alt = "-"
style = "Classical"

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Anarchy",         _("Usurper %s"),        _("?female:Usurper %s")
 "Despotism",       _("Despot %s"),         _("?female:Despot %s")
 "Fundamentalism",  _("Elder %s"),          _("?female:Elder %s")
}

init_techs=""
init_buildings=""
init_units=""

conflicts_with="hellenic", "byzantine", "roman", "ottoman", "turkish", "venetian",
               "italian"
civilwar_nations = "cretan", "greek" ; carian

cities =
  "Pharsalos",
  "Korinthos",
  "Zakynthos",
  "Athenai",
  "Mykenai",  
  "Amarynthos",
  "Tirynsos",
  "Brilettos",
  "Lykabettos",
  "Gargettos",
  "Larissa",
  "Parnassos",
  "Kephissos",
  "Ilissos",
  "Amnissos",
  "Tylissos",
  "Messene",
  "Kyllene",
  "Kyrene",
  "Mytilene",
  "Thebes",
  "Delphi",
  "Lindos",
  "Rhamnos"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
