# Freeciv(nation) · metis

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/metis.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的metis定义

## 正文
```ruleset
[nation_metis]

name=_("Métis")
; pre-2.6 had plain ASCII names
rule_name="Metis"
plural=_("?plural:Métis")
groups="American"
legend=_("The Métis are a people of mixed First Nations (Native American)\
 and European (mostly French) descent living mainly in the Canadian\
 prairie provinces. Together with the First Nations and the Inuit they\
 form one of the three indigenous groups of Canada. In the 19th century\
 the Métis repeatedly rebelled against the British and Canadian\
 authorities.")

leaders = {
 "name",                        "sex"
 "Toussaint Charbonneau",       "Male"
 "Gabriel Dumont",              "Male"
 "Louis Riel",                  "Male"
 "James P. Brady",              "Male"
 "Blanche Brillon Macdonald",   "Female"
}

flag="metis"
flag_alt="-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="quebecois", "cree", "acadian"

cities =
 "Batoche",
 "Sault Ste. Marie",
 "Prince Albert",
 "Assiniboia",
 "Battleford",
 "Fish Creek",
 "Cut Knife",
 "Frenchman's Butte",
 "Duck Lake",
 "Loon Lake",
 "Frog Lake",
 "Fort Garry",
 "Lower Fort Garry",
 "Buffalo Lake",
 "Kikino",
 "Paddle",
 "Gift Lake",
 "Fishing Lake",
 "East Prairie",
 "Peavine",
 "Elizabeth",
 "Fort Carlton",
 "Fort Pitt",
 "Selkirk",
 "Sputinow",
 "Pembina",
 "Portage la Prairie",
 "Seven Oaks",
 "Fort Frances"



```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
