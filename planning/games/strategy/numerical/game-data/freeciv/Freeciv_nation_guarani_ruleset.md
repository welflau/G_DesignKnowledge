# Freeciv(nation) · guarani

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/guarani.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的guarani定义

## 正文
```ruleset
[nation_guarani] 

name=_("Guarani") 
plural=_("?plural:Guarani") 
groups="American" 
legend=_("Numbering perhaps as many as 400,000 people at the time\
 of European contact, the Aba (more popularly known as Guarani) lived\
 primarily in what is now Paraguay in agricultural villages. Today their\
 Guarani language is spoken by over 4 million people and is an official\
 language of the nation of Paraguay.") 

leaders = {
 "name",                "sex"
 "Sepe Tiaraju",        "Male"
 "Nheçu",               "Male"
 "Nicolás Ñanguirú",    "Male"
 "Miguel Guarumba",     "Male"
}

flag = "guarani" 
flag_alt = "-" 
style = "Tropical" 

init_techs="" 
init_buildings="" 
init_units="" 

conflicts_with="dutch"
civilwar_nations="akwe", "tupi", "aymara" 

cities = 
"Akã'ai", 
"Ka'akupe", 
"Mbarakaju", 
"Ka'asapa", 
"Sapukái", 
"Yvy ja'u", 
"Tujuti", 
"Jasyretã", 
"Ypakarai", 
"Kapiatã", 
"Amambái", 
"Yguasu", 
"Kurupa'yty", 
"Itapúa", 
"Yvyku'i", 
"Itakuruvi", 
"Ykuamandyju", 
"Itaipu", 
"Yvytymi", 
"Ysoso", 
"Kambyretã", 
"Minas kue", 
"Ñe'embuku", 
"Ka'aguasu"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
