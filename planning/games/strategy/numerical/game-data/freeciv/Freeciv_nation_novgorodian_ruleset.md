# Freeciv(nation) · novgorodian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/novgorodian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的novgorodian定义

## 正文
```ruleset
[nation_novgorodian]

name=_("Novgorodian")
plural=_("?plural:Novgorodians")
groups="European", "Medieval"
legend=_("The Novgorod Republic was was a large Medieval Russian state\
 that stretched from the Baltic Sea to the Ural Mountains. It existed\
 between the 12th and 15th centuries and was centered on the city of\
 Novgorod.")
leaders = {
 "name",                    	"sex"
 "Burivoi",		    	"male"
 "Riurik",		    	"male"
 "Gleb Sviatoslavich",	    	"male"
 "Sviatopolk Iziaslavich",  	"male"
 "Vsevolod Mstislavich",    	"male"
 "Rostislav Iurevich",	    	"male"
 "Sviatoslav Ol'govich",	"male"
 "Iaroslav Iziaslavich",	"male"
 "Rostislav Mstislavich",	"male"
 "Roman Mstislavich",		"male"
 "Mstislav Rostislavich",	"male"
 "Iaroslav Vladimirovich",	"male"
 "Konstantin Vsevolodich",	"male"
 "Fedor Iaroslavich",		"male"
 "Aleksandr Iaroslavich",	"male"           ;Aleksandr Nevsky
 "Dmitry Aleksandrovich",	"male"
 "Semen Ivanovich",		"male"
 "Lengvenis Olgerdovich",	"male"
 "Vasily Dmitr'evich",		"male"
 "Jonas Vladimiraitis",		"male"
 "Marfa Boretskaya",		"female"
}
flag= "novgorod" 
flag_alt = "-" 
style = "European"
ruler_titles = {
"government",     "male_title",         "female_title"
"Democracy",      _("Councillor %s"),   _("?female:Councillor %s")
"Despotism",      _("Prince %s"),       _("Princess %s")
"Monarchy",       _("Grand Prince %s"), _("Grand Princess %s")
"Fundamentalism", _("Patriarch %s"),    _("Matriarch %s")
"Republic",       _("Burgomaster %s"),  _("?female:Burgomaster %s")
} 
init_techs=""
init_buildings=""
init_units=""

conflicts_with="soviet"
civilwar_nations="muscovite", "komi", "karelian"

cities =
 "Veliky Novgorod",
 "Pskov",
 "Arhangelsk",
 "Novorzhev",
 "Perm",
 "Pechora",
 "Yugra",
 "Tre",
 "Zavolchye",
 "Bezhetsk",
 "Staraya Ladoga",
 "Porkhov",
 "Koporye",
 "Yama",
 "Oreshek",
 "Korela",
 "Volkolamsk",
 "Torzhok",
 "Podberezhe",
 "Volhov",
 "Cherepovec",
 "Syktyvkar",
 "Uhta",
 "Velikiye Luki",
 "Narva",
 "Bolotovo"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
