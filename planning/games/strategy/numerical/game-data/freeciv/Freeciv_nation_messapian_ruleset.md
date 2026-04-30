# Freeciv(nation) · messapian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/messapian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的messapian定义

## 正文
```ruleset
[nation_messapian]

name=_("Messapian")
plural=_("?plural:Messapians")
groups="Ancient", "European"
legend=_("The Messapii were an Indo-European tribe that inhabited, in\
 ancient times, Apulia, the south-eastern peninsula of Italy, before being\
 absorbed by the Romans.")
leaders = {
 "name",     "sex"
 "Opis",     "Male"
 "Artas",    "Male"
 "Dasius",   "Male"
}
flag="messapian"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Italian", "Western Roman", "Ostrogothic", "Neapolitan"
civilwar_nations = "Samnite", "Illyrian", "Greek", "Roman"

cities =
 "Oria",
 "Kailia",
 "Alytia",
 "Salapia",
 "Uzenton",
 "Rudiai",
 "Brention",
 "Hyreton",
 "Myron",
 "Idruntum",
 "Manduria",
 "Mesania",
 "Neriton",
 "Sybar",                   ;Cavallino
 "Thurria Sallentina",
 "Barion",
 "Fovea",                   ;Foglia
 "Aikai",
 "Aoxentum"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
