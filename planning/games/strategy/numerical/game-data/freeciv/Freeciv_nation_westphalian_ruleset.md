# Freeciv(nation) · westphalian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/westphalian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的westphalian定义

## 正文
```ruleset
[nation_westphalian]

name=_("Westphalian")
plural=_("?plural:Westphalians")
groups="Medieval", "European"
legend=_("Westphalia, before becoming a Prussian province, was the western\
 region of the Duchy of Saxony. Today it makes up the northern part of\
 the largest German federal state, North Rhine-Westphalia.")

leaders = {
 "name",                        "sex"
 "Widukind",                    "Male"
 "Liudger",                     "Male"
 "Hermann von Werl",            "Male"
 "Gottfried von Arnsberg",      "Male"
 "Adolf III von der Mark",      "Male"
 "Heinrich Aldegrever",         "Male"
 "Jan van Leiden",              "Male"
 "Franz von Waldeck",           "Male"
 "Bernhard von Galen",		"Male"
 "Hieronymus Napoleon",		"Male"
 "Annette von Droste Hülshoff", "Female"
}

flag="westphalia"
flag_alt = "germany"
style = "European"

ruler_titles = {
 "government",     "male_title",            "female_title"
 "Despotism",      _("Duke %s"),            _("Duchess %s")
 "Fundamentalism", _("Prince-Bishop %s"),   _("Princess-Bishop %s")
 "Monarchy",       _("Grand Duke %s"),      _("Grand Duchess %s")
 "Republic",       _("Burgomaster %s"),     _("?female:Burgomaster %s") 
}


init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Hanoverian", "Lippian", "Saxon", "Rhenish"

cities =
 "Münster",
 "Dortmund",
 "Bochum",
 "Bielefeld",
 "Gelsenkirchen",
 "Hagen", 
 "Hamm",
 "Herne",
 "Paderborn",
 "Recklinghausen",
 "Bottrop",
 "Siegen",
 "Arnsberg",
 "Bocholt",
 "Gütersloh",
 "Herford",
 "Iserlohn",
 "Lippstadt",
 "Lüdenscheid",
 "Lünen",
 "Menden",
 "Minden",
 "Rheine",
 "Soest",
 "Warendorf",
 "Werl",
 "Ahaus",
 "Borken",
 "Coesfeld",
 "Steinfurt",
 "Schwelm",
 "Meschede",
 "Olpe",
 "Unna",
 "Höxter",
 "Lübbecke",
 "Gronau",
 "Bad Laasphe",
 "Tecklenburg",
 "Castrop-Rauxel",
 "Gladbeck",
 "Witten",
 "Dorsten",
 "Herten",
 "Marl",
 "Bad Oeynhausen",
 "Winterberg",
 "Warstein"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
