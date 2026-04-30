# Freeciv(nation) · numidian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/numidian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的numidian定义

## 正文
```ruleset
[nation_numidian]

name=_("Numidian")
plural=_("?plural:Numidians")
groups="Ancient", "African"

legend=_("The Numidians were an ancient Berber people renowned for their\
 horsemanship who were composed of two main tribes in modern Algeria and\
 Tunisia: the Massyli in the east and the Massaesyli in the west. They were\
 united under King Massinissa, whose position was guaranteed by his Roman\
 allies after the 2nd Punic War in which he aided the Romans in their defeat\
 of the Carthaginians. His unified kingdom was short-lived, however, as the\
 west was given to the Mauretanian king by the Romans following the death of\
 King Jugurtha. Eventually all of Numidia and Mauretania were added to the\
 Roman realm.")

leaders = {
 "name",        "sex"
 "Syphax",      "Male"
 "Massinissa",  "Male"
 "Jugurtha",    "Male"
 "Micipsa",     "Male"
 "Gala",        "Male"
}

flag="numidia"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="carthaginian", "algerian"

cities =
 "Cirta",
 "Capsa",
 "Thugga",
 "Bulla",
 "Mediae",
 "Thabudis",
 "Capsa",
 "Tamalleni",
 "Nepte",
 "Thiges",
 "Thala",
 "Lambes",
 "Sibesua",
 "Justi",
 "Tibilis",
 "Mopti",
 "Naraggara",
 "Thagaste",
 "Sitifi",
 "Calama",
 "Milevi",
 "Nedes",
 "Cerva",
 "Vegeste",
 "Claudi",
 "Zama",
 "Theveste",
 "Vasidica",
 "Thusurus",
 "Lamasba"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
