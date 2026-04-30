# Freeciv(nation) · chimu

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/chimu.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的chimu定义

## 正文
```ruleset
[nation_chimu] 

name=_("Chimu") 
plural=_("?plural:Chimu") 
groups="Medieval", "American" 
legend=_("Inheritors of the Moche cultural tradition, Chimor began\
 its expansion in the 12th century from the Moche river valley in\
 what is now northern Peru. Their expansion continued until they\
 were halted and conquered by the rising Inka Empire in 1470. Their\
 last king, Minchancaman, was captured and led to the Inka capital\
 Qosqo. Chimu artisans contributed greatly to the manufacture of Inka\
 artistic wares. Until its fall, Chimor controlled perhaps 2/3 of\
 the population of the northern Andes.") 

leaders = {
 "name",                "sex"
 "Tacaynamu",           "Male"
 "Guacricaur",          "Male"
 "Ñanenpinco",          "Male"
 "Minchançaman",        "Male"
 "Fempellec",           "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("Lord %s"),      _("Lady %s")
}

flag= "chimu" 
flag_alt = "-" 
style = "Babylonian" 

init_techs="" 
init_buildings="" 
init_units="" 

civilwar_nations="inca", "aymara", "mwiska"

cities = 
"Chan Chan", 
"Farfán", 
"Pacatnamú", 
"Sican", 
"Manchán", 
"Cinto", 
"Túcume", 
"Juayanca", 
"Chotuna", 
"Batan", 
"Mocollope", 
"Galindo", 
"Huancaco", 
"Panamarca", 
"Cao", 
"Piura", 
"Chiclayo", 
"Huamachuco", 
"Apurlé", 
"Piura", 
"Payta", 
"Pacasmayo", 
"Viru"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
