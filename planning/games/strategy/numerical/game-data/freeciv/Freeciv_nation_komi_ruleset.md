# Freeciv(nation) · komi

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/komi.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的komi定义

## 正文
```ruleset
[nation_komi] 

name=_("Komi") 
plural=_("?plural:Komi") 
groups="European", "Medieval"
legend=_("The Komi are a Finno-Ugric people living in the northern part of\
 European Russia. In the Middle Ages, the area inhabited by people of Komi\
 was dominated by the Republic of Novgorod. In the 15th century, the Komi\
 were subordinated to Moscow, becoming part of Russia.")
leaders = {
 "name",                    "sex"
 "Perymsa Stefan",          "male"
 "Pama",                    "male"
 "Ölösh Kuratov",           "male"
 "Yuri Spiridonov",         "male"
 "Ölöksan Volod Torlopov",  "male"  ;Vladimir Torlopov
 "Marina Istikhovskaya",    "female"
}

flag= "komi" 
flag_alt = "-" 
style = "Celtic"

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Fundamentalism",  _("Great Shaman %s"), _("?female:Great Shaman %s")
}
init_techs="" 
init_buildings="" 
init_units="" 

civilwar_nations = "mordvin", "Muscovite" ;novgorodian

cities =
 "Syktyvkar",
 "Uskar",
 "Ukva",                  ;Uhta
 "Inta",
 "Vörkuta",               ;Vorkuta
 "Vuktyl",
 "Parma",
 "Aykatyla",
 "Emba",
 "Izva",
 "Koygort",
 "Körtkerös",
 "Kulomdyn",
 "Abyachoy",
 "Myldyn",
 "Sösnagort",
 "Vizin",
 "Vylgort",
 "Koslan",
 "Chilimdyn",
 "Sedkyrkeshch",
 "Kozhym",
 "Pechöra",
 "Izyyayu",
 "Kozhva",
 "Voyvozh",
 "Shudayag",
 "Yarega",
 "Vorgashor",
 "Mikun",
 "Zheshart"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
