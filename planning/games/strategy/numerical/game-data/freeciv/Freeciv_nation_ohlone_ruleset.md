# Freeciv(nation) · ohlone

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/ohlone.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的ohlone定义

## 正文
```ruleset
[nation_ohlone] 
name=_("Ohlone") 
plural=_("?plural:Ohlone") 
groups="American" 
legend=_("Gatherers, hunters and fishermen, the Ohlone lived in\
 over 40 bands stretching from the San Francisco Bay south to the\
 Salinas Valley. They spoke eight distinct yet related languages\
 and though they shared many cultural traits common to other Native\
 Californian peoples, the Ohlone were also diverse in some finer\
 aspects of culture. Their way of life changed dramatically when the\
 Spanish arrived in 1769 and disease and the injustices of Mission\
 life came to replace their earlier lives. Though the last fluent speaker\
 of an Ohlone language died in 1939, the Ohlone are today federally\
 recognized as 7 tribes.") 

leaders = {
 "name",        "sex"
 "Chamis",      "Male"
 "Xigmacse",    "Male"
 "Mossués",     "Male"
 "Charquín",    "Male"
}
ruler_titles = {
 "government",      "male_title",            "female_title"
 "Democracy",       _("Principal Chief %s"), _("?female:Principal Chief %s")
 "Fundamentalism",  _("Shaman %s"),          _("?female:Shaman %s")
 "Monarchy",        _("Great Chief %s"),     _("?female:Great Chief %s")
}
flag= "ohlone" 
flag_alt = "-" 
style = "Celtic" 

init_techs="" 
init_buildings="" 
init_units="" 

civilwar_nations="nuu-chah-nulth", "hopi", "chumash"

cities = 
"Aleitac", 
"So-co-is-u-ka", 
"Pruristac", 
"Amuctac", 
"Petlenuc", 
"Sitlintac", 
"Tubsinta", 
"Tuchayune", 
"Puichon", 
"Somontac", 
"Thamien", 
"Altahmo", 
"Luecha", 
"Achista", 
"Chatu-mu", 
"Chaloctac", 
"Partacsi", 
"Aptos", 
"Chutchui", 
"Timigtac", 
"Rumsen", 
"Uypi", 
"Wacharon", 
"Mutsun", 
"Wachero-n", 
"Uturbe"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
