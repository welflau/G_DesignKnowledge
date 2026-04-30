# Freeciv(nation) · ozite

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/ozite.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的ozite定义

## 正文
```ruleset
[nation_ozite]

name=_("Ozite")
plural=_("?plural:Ozites")
groups="Imaginary"
; Baum’s books were published before 1923 and are therefore out of
; copyright.
legend=_("The land of Oz was created by L. Frank Baum in 1900 in 'The\
 Wonderful Wizard of Oz' and was subsequently embellished in a number\
 of other books. The country consists of four main territories: Winkie\
 Country, Quadling Country, Munchkin Country, and Gillikin Country. Oz\
 is surrounded by an impassable desert.")

leaders = {
 "name",                "sex"
 "Ozma",                "Female" ; a.k.a. Tip
 "Pastoria",            "Male" ; Ozma’s father
 "Lurline",             "Female" ; The fairy queen
 "O. Z. Diggs",         "Male" ; a.k.a. The wonderful wizard
 "Scarecrow",           "Male" ; Successor to the wizard
 "Dorothy Gale",        "Female" ; Not a ruler, but a popular character
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Despotism",       _("Wizard %s"),      _("Witch %s")
}

flag="oz"
style = "European"

init_techs=""
init_buildings=""
init_units=""

cities =
 "Emerald City",
 "Munchkin",
 "Winkie",
 "Gillikin",
 "Quadling",
 "Shiz",
 "Bunbury",
 "Bunnybury",
 "Center Munch",
 "Ovvels",
 "Qhoyre",
 "Bright Lettins",
 "Old Pastoria",
 "Three Dead Trees",
 "Broad Slope Town",
 "Stonespar End",
 "Colwen Grounds",
 "Dragon Cupboard",
 "Upper Applerue",
 "Far Applerue",
 "Neverdale",
 "Rigmarole",
 "Utensia",
 "Bengda",
 "Rush Margins",
 "Center Bounty",
 "Colwen Grounds",
 "Brox Hall",
 "Tenniken",
 "Traum",
 "Frottica",
 "Wittica",
 "Settica",
 "Wiccasand Turning",
 "Welcome Arms",
 "Fanarra",
 "Upper Fanarra",
 "Red Windmill",
 "Horners",
 "Hoppers",
 "Flutterbudget",
 "Tottenhots",
 "Mn Yoop",
 "Fuddlecumjig",
 "Hammerheads"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
