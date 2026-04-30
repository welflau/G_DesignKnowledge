# Freeciv(nation) · belarusian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/belarusian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的belarusian定义

## 正文
```ruleset
[nation_belarusian]

name=_("Belarusian")
plural=_("?plural:Belarusians")
groups="Modern", "European"
legend=_("Belarus was part of the ancient Slavic state of Kievan Rus', then\
 subsequently Lithuania, Rzeczpospolita, the Russian Empire and the Soviet\
 Union. Belarus became independent in 1991 with the dissolution of the\
 Soviet Union.")

leaders = {
 "name",                        "sex"

; The most famous ruler of Polatsak.
 "Usyaslav Brachyslavich",      "Male"

; also known as Vytautas the Great, see lithuanian.ruleset
 "Vitaut",                      "Male"

; the printer of first book in Belarusian language
 "Francysk Skaryna",            "Male"

; the Grand Hetman of Lithuania
 "Mikalaj Radzivil",            "Male"

; the leader of the January Uprising in Belarus
 "Kastus Kalinouski",           "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("Duke %s"),      _("Duchess %s")
 "Monarchy",        _("Tsar %s"),      _("Tsaritsa %s")
 "Fundamentalism",  _("Patriarch %s"), _("Matriarch %s")
}

flag="belarus"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="russian", "lithuanian", "polish", "ukrainian"

cities =
  "Minsk",
  "Homyel",
  "Vitsyebsk",
  "Polatsak",
  "Mahilyow",
  "Orsha",
  "Brest",
  "Hrodna",
  "Barysaw",
  "Niasvizh",
  "Pastavy",
  "Lyepyel'",
  "Maladzyechna",
  "Lida",
  "Krychaw",
  "Asipovichy",
  "Babruysk",
  "Pinsk",
  "Slutsk",
  "Salihorsk",
  "Zhlobin",
  "Vawkavysk",
  "Slonim",
  "Baranavichy",
  "Kobryn",
  "Byaroza",
  "Luninyets",
  "Zhytkavichy",
  "Mazyr",
  "Rechytsa"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
