# Freeciv(nation) · cossack

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/cossack.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的cossack定义

## 正文
```ruleset
[nation_cossack] 

name=_("Cossack") 
plural=_("?plural:Cossacks") 
groups="European", "Early Modern"
legend=_("The Zaporozhian Cossacks lived in Zaporozhia, in Central\
 Ukraine. They were a multi-ethnic community with Ruthenians being the\
 dominant element, organized in a military manner.")

leaders = {
 "name",                        "sex"
 "Predslav Lyantskoronsky",     "Male"
 "Ostap Dashkevych",            "Male"
 "Dmytro Vyshnevetsky",         "Male"
 "Ivan Svirgovsky",             "Male"
 "Ivan Pidkova",                "Male"
 "Kryshtof Kosynsky",           "Male"
 "Ivan Sulyma",                 "Male"
 "Bohdan Khmelnytsky",          "Male"
 "Ivan Bohun",                  "Male"
 "Ivan Mazepa",                 "Male"
 "Pavlo Polubotok",             "Male"
 "Kyrylo Rozumovsky",           "Male"
 "Yemelyan Pugachev",           "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("Prince %s"),       _("Princess %s")
 "Monarchy",        _("Grand Prince %s"), _("Grand Princess %s")
 "Republic",        _("Hetman %s"),       _("?female:Hetman %s")
 "Fundamentalism",  _("Patriarch %s"),    _("Matriarch %s")
}

flag= "cossack" 
flag_alt = "-" 
style = "Celtic" 

init_techs="" 
init_buildings="" 
init_units="" 

conflicts_with = "ukrainian"
civilwar_nations = "ukrainian", "russian", "crimean tatar", "volga german"

cities =
 "Chyhyryn",
 "Zaporizhzhia",
 "Stara Sich",
 "Nova Sich",
 "Hlukhiv",
 "Kyiv",
 "Nizhyn",
 "Terek",
 "Azov",
 "Tsaritsyn",
 "Astrakhan",
 "Vladikavkaz",
 "Kamyshin",
 "Orenburg",
 "Sevastopol",
 "Mozdok",
 "Baturyn"

; More cities will be fetched from above nations

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
