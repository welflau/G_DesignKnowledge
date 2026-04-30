# Freeciv(nation) · chumash

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/chumash.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的chumash定义

## 正文
```ruleset
[nation_chumash] 

name=_("Chumash") 
plural=_("?plural:Chumash") 
groups="American"
legend=_("Inhabiting the Santa Barbara Channel Islands and the southern\
 California coastline between Malibu and Paso Robles inland towards the San\
 Joaquin valley, the Chumash lived in large permanent villages and maintained\
 a semi-monetized economy. These villages came to be ruled by hereditary\
 chiefs, who could be male or female. At time of contact, the population was\
 likely 8-18,000 people, though perhaps as high as 22,000. The Spanish\
 established five missions in Chumash land. As a result of disease and other\
 byproducts of colonial rule, the population fell to less than 3,000 in 1831.")

leaders = {
 "name",        "sex"
 "Yanonalit",   "Male"
 "Kitsepawit",  "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Monarchy",        _("Great Chief %s"),     _("?female:Great Chief %s")
 "Fundamentalism",  _("Shaman %s"),          _("?female:Shaman %s")
 "Democracy",       _("Principal Chief %s"), _("?female:Principal Chief %s")
}

flag = "chumash"
flag_alt = "-" 
style = "Celtic" 

init_techs="" 
init_buildings="" 
init_units="" 
civilwar_nations="hopi", "ohlone"

cities = 
"Syuxtun", 
"Xonxon’ata", 
"Lompo’", 
"Niaqla", 
"Tuqan", 
"Shawa", 
"Xaxas", 
"Lisiqishi", 
"Sis’a", 
"Kashtiq", 
"Stuk", 
"Texax", 
"‘Ataxis", 
"Chimimu’", 
"Chihlkukunach", 
"Wasna", 
"Lalimanux", 
"Nanawani", 
"Heqep", 
"Hawamiw", 
"Washlayik", 
"Tashlipun", 
"Tso", 
"Helewashkuy", 
"Mikiw", 
"Chanu", 
"Kach’antuk’", 
"Huwam", 
"Achililiwo", 
"Shnaxalyiwi"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
