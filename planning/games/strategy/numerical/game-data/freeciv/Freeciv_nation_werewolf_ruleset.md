# Freeciv(nation) · werewolf

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/werewolf.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的werewolf定义

## 正文
```ruleset
[nation_werewolf]

; To avoid any trademark complaints, no modern fictional works are used.
name=_("Werewolf")
plural=_("?plural:Werewolves")
groups="Imaginary"
legend=_("A werewolf is a human who under certain circumstances is\
 transformed into a wolf-like beast. During the Middle Ages in Europe,\
 werewolves were believed to terrorize villages in search of human flesh\
 and were often blamed for unexplained or particularly brutal killings.")

leaders = {
 "name",                "sex"

; Fictional werewolves
 "Bisclavret",          "Male" ; from "Bisclavret"
 "Alfonso",             "Male" ; from "Guillaume de Palerme"

; Historical persons associated with lycanthropy
 "Thiess",              "Male" ; Livonian commoner accused of lycanthropy
 "Vseslav",             "Male" ; Belarusan prince
 "Vereticus",           "Male" ; Welsh king

; From Greek legend...
 "Demaenetus",          "Male"
 "Damarchus",           "Male"
 "Lycaon",              "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Republic",        _("%s Alpha"),        _("?female:%s Alpha")
}

flag="luna"
flag_alt="-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Chananean"

cities =
 "Lycopolis",
 "Arcadia",

; Cities associated with werewolf incursion
 "Magdeburg",		; associated with the Wolf of Magdeburg
 "Langogne",		; associated with the Beast of Gévaudan
 "Bedburg",		; associated with Peter Stumpp 
 "Dole",		; associated with Gilles Garnier
 "Jurgenburg",		; associated with Theiss
 "Elkhorn",		; associated with the Beast of Bray Road
 "Vastemoisa",		; associated with Libbe Matz

; Sites of noted wolf attacks
 "Kirov",
 "Ansbach",
 "Ashta",
 "Gysinge",
 "Soissons",
 "Hazaribagh",
 "Périgueux",
 "Turku",
 "Sarlat",

; Wolfs in mythology
 "Roma",		; Romulus and Remus were raised by a wolf
 "Ötüken",		; Göktürks
 "Járnviðr",		; Forest inhabited by wolfs in Norse mythology
 "Gubbio"		; Francis of Assisi tamed a wolf there

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
