# Freeciv(nation) · chickasaw

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/chickasaw.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的chickasaw定义

## 正文
```ruleset
[nation_chickasaw]

name=_("Chickasaw")
plural=_("?plural:Chickasaws")
groups="Early Modern", "American"
legend=_("One of the so-called Five Civilized Tribes, the Chickasaw\
 occupied primarily what is today the northern part of the U.S. state of\
 Mississippi at the time of first contact with Europeans. The name\
 \"Mississippi\" itself originates from a Chickasaw word meaning\
 \"Without Source.\"")
 
leaders = {
 "name",                         "sex"
 "Holmes Colbert",               "Male"
 "Fred Waite",                   "Male"
 "Tishomingo",                   "Male"
 "George Colbert",               "Male"
 "Itawamba",                     "Male"
 "Taski Etoka",                  "Male"
}
flag="chickasaw"
flag_alt="-"
style = "Celtic"

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Monarchy",        _("Great Chief %s"),     _("?female:Great Chief %s")
 "Republic",        _("Spokesman %s"),       _("Spokeswoman %s")
 "Democracy",       _("Principal Chief %s"), _("?female:Principal Chief %s")
}

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Cherokee", "Muskogee", "Choctaw"

cities =
; Old Mississippi settlements http://www.accessgenealogy.com/native/tribes/chickasaw/chickasawhist.htm
 "Shatara",
 "Chook'heereso",
 "Hykehah",
 "Tuskawillao",
 "Phalacheho",
 "Yaneka",
 "Chookka Pharáah",
 "Amalahta",
 "Chatelaw",
 "Chukafalaya",
 "Hikkihaw",
 "Chucalissa",
 "Tuckahaw",
 "Ashukhuma",
; After Indian Removal, in Oklahoma
 "Tishomingo",
 "Pontotoc",
 "Pickens",
 "Ponola"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
