# Freeciv(nation) · jolof

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/jolof.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的jolof定义

## 正文
```ruleset
[nation_jolof] 

name=_("Jolof") 
plural=_("?plural:Jolof") 
groups="Medieval", "Early Modern", "African" 
legend=_("Also called Wolof, the Kingdom was formed between the\
 Senegal and Gambia rivers in the 14th century. The King, or Burba\
 Jolof, was beholden to a handful of powerful regional noblemen who\
 acknowledged kinship with the king but developed personal power\
 bases as well. By the early 1500s, the Burba Jolof could field as\
 many as 100,000 infantry and 10,000 cavalry. Fulani and Berber\
 incursions coupled with political weakness eroded away the power\
 of the Burba Jolof. Various Wolof-speaking states established\
 unions with one another, with their heads assuming the powers of\
 Burba Jolof. The 19th century brought with it French colonization\
 and a conversion to Islam fueled in large part by anti-European\
 sentiment.") 

leaders = {
 "name",                "sex"
 "Ndyadyane Ndyaye",    "Male"
 "Sare N'Dyaye",        "Male"
 "Gireun Buri Dyelen",  "Male"
 "Bukaar Biye-Sungule", "Male"
 "Lat-Koddu",           "Male"
}

flag= "jolof" 
flag_alt = "-" 
style = "Tropical" 

init_techs="" 
init_buildings="" 
init_units="" 

civilwar_nations="malian", "senegalese" 

cities = 
"Linguère", 
"Kaolack", 
"Louga", 
"Dagana", 
"Rosso", 
"Dara", 
"Kanifing", 
"Koki", 
"Mekhé", 
"Mboro", 
"Kébémèr", 
"Mpal", 
"Lagbar", 
"Toubu", 
"Gassane", 
"Joal-Fadiat", 
"Pikine", 
"Vélingara", 
"Tiel", 
"Sokone", 
"Mbour", 
"Farafenni", 
"Bambey", 
"Bogué", 
"Podor", 
"Kerewan", 
"Fatick", 
"Yoff"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
