# Freeciv(nation) · aleut

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/aleut.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的aleut定义

## 正文
```ruleset
[nation_aleut]

name=_("Aleut")
plural=_("?plural:Aleuts")
groups="American", "Asian"
legend=_("The Unangan, or Aleut, lived in permanent subterranean homes\
 in their hunting and fishing villages. They lived in the Aleutian\
 islands for thousands of years prior to European contact. Unangan people\
 developed ties to Russian missionaries and traders many converting to\
 Russian Orthodox Christianity and intermarrying with Russians, and some\
 even accompanied Russians to their other colonial entrepots such as Ft.\
 Ross in northern California and Ft. Elizabeth in Hawai'i.")

leaders = {
 "name",                "sex"
 "Ivan Pan'kov",        "Male"
 "AhKahNeKak",          "Male"
 "Igadik",              "Male"
}

ruler_titles = {
 "government",     "male_title",     "female_title"
 "Fundamentalism", _("Shaman %s"),   _("?female:Shaman %s")
}

flag="aleut" 
flag_alt = "-" 
style = "celtic" 

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "inuit", "nuu-chah-nulth", "cree"

cities = 
"Akutan", 
"Unalaska", 
"Sanak", 
"Mackushin", 
"Kashega", 
"Adaq", 
"Umnak", ; Nikolski 
"Qagun Tayagungin", 
"Akun", 
"Unimak", 
"Aikhag", 
"Aiaialgutak", ; Avatanak 
"Ugamak", 
"Tigalda", 
"Agattu", 
"Attu", 
"Amchitka", 
"Ulak", 
"Amatignak", 
"Atka"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
