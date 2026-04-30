# Freeciv(nation) · hasinay

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/hasinay.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的hasinay定义

## 正文
```ruleset
[nation_hasinay] 

name=_("Hasinay") 
plural=_("?plural:Hasinay") 
groups="American"
legend=_("A Caddoan political league from East Texas, the Hasinay\
 Confederacy consisted of a group of agricultural villages. Though they were\
 involved in trade networks connecting them with people as far west as the\
 Puebloan polities of the American Southwest, their cultural ties were more\
 strongly in line with the other mound-building cultures of the Southeast.\
 The word Texas is derived from Caddoan word for \"Friend.\"")

leaders = {
 "name",                "sex"
 "LaRue Parker",        "Female"
 "Vernon Hunter",       "Male"
 "Donnie Frank",        "Male"
 "Henry Shemayme",      "Male"
 "Hubert Halfmoon",     "Male"
 "Melford Williams",    "Male"
 "Nah-ah-sah-nah",      "Male"
 "Sho-ee-tat",          "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Democracy",       _("Principal Chief %s"), _("?female:Principal Chief %s")
 "Fundamentalism",  _("Shaman %s"),          _("?female:Shaman %s")
 "Monarchy",        _("Great Chief %s"),     _("?female:Great Chief %s")
 "Republic",        _("Spokesman %s"),       _("Spokeswoman %s")
}

flag="caddo" 
flag_alt = "-" 
style = "tropical" 

init_techs="" 
init_buildings="" 
init_units="" 

civilwar_nations = "hopi", "muskogee", "sioux"

cities = 
"Nabedache", 
"Anadarko", 
"Neches", 
"Yscani", 
"Nechaui", 
"Tadiva", 
"Nacono", 
"Ais", 
"Nacau", 
"Kichai", 
"Nacogdoche", 
"Guasco", 
"Nasoni", 
"Hainai", 
"Nadaco", 
"Nabiti", 
"Nacachau", 
"Nacanish", 
"Namidish", 
"Yatasi", 
"Naansi", 
"Nabeyeyxa", 
"Nadamin", 
"Natsshostanno", 
"Neihahat"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
