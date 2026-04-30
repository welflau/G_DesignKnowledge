# Freeciv(nation) · aramean

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/aramean.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的aramean定义

## 正文
```ruleset
[nation_aramean] 

name=_("Aramean") 
plural=_("?plural:Arameans") 
groups="Ancient", "Asian" 
legend=_("According to legend, the Aramean people are the descendants of\
 Aram, the grandson of Noah.") 

leaders = {
 "name",        "sex"
 "Ahuni",       "Male"
 "Kapara",      "Male"
 "Barrakib",    "Male"
 "Bar Hadad",   "Male"
 "Hasael",      "Male"
 "Zenobia",     "Female"
 "Aryo",        "Male"
 "Abgar VIII",  "Male" ; a.k.a. Abgar the Great
}

flag="aram" 
flag_alt = "-" 
style = "Classical" 

init_techs="" 
init_buildings="" 
init_units="" 
civilwar_nations = "assyrian", "babylonian", "palmyrene"

cities = 
 "Aram",
 "Amid",
 "Mardin",
 "Commagene",
 "Urhoi", 
 "Haran",
 "Melitene",
 "Nisibin",
 "Guzana",
 "Yamkhat",
 "Hama", 
 "Homs",
 "Damascus",
 "Tadmor",
 "Ebla", 
 "Midyat",
 "Tikrit",
 "Bethsaida" 

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
