# Freeciv(nation) · brandenburgian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/brandenburgian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的brandenburgian定义

## 正文
```ruleset
[nation_brandenburgian]

name=_("Brandenburgian")
plural=_("?plural:Brandenburgians")
groups="Medieval", "Early Modern", "European"
legend=_("Formerly the Northern March of East Francia, Brandenburg became\
 an electorate of the Holy Roman Empire in the 12th century. The rulers of\
 Brandenburg acquired Prussia in 1618 and was absorbed by Prussia in 1701.\
 Brandenburg kept its nominal independence until 1806, when it became\
 a province of Prussia. Currently it is one of the states of the Federal\
 Republic of Germany.")
leaders = {
"name",			"sex"
"Gero",			"male"
"Albrecht der Bär",	"male"
"Otto I",		"male"
"Ludwig I",		"male"
"Friedrich",		"male"
"Friedrich II",		"male"
"Anna",			"female"
"Albrecht Friedrich",	"male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Communism",       _("First Secretary %s"), _("?female:First Secretary %s")
 "Despotism",       _("Margrave %s"),        _("Margravine %s")
 "Fundamentalism",  _("Archbishop %s"),      _("Mother Superior %s")
 "Monarchy",        _("Elector %s"),         _("Electress %s")
 "Democracy",  _("Minister-President %s"), _("?female:Minister-President %s")
}

flag="brandenburg" 
flag_alt = "-" 
style = "european" 

init_techs="" 
init_buildings="" 
init_units="" 

conflicts_with = "hessian" ;similar flag
civilwar_nations = "prussian", "sorbian", "veletian"

cities = 
"Brandenburg an der Havel (river)",
"Potsdam",
"Berlin",
"Frankfurt/Oder (river)",
"Spandau",
"Cottbus",
"Eberswalde",
"Forst",
"Rathenow",
"Guben",
"Wittenberge",
"Landsberg",
"Cölln",
"Neubrandenburg",
"Köpenick",
"Prenzlau",
"Schwedt/Oder (river)",
"Charlottenburg",
"Neuruppin",
"Soldin",
"Torgau",
"Bautzen",
"Merseburg",
"Bernstein",
"Oranienburg",
"Driesen",
"Wittstock",
"Lübben",
"Herzberg",
"Seelow",
"Senftenberg",
"Beeskow",
"Bad Belzig",
"Perleberg",
"Luckenwalde",
"Bernau",
"Königs Wusterhausen",
"Pasewalk",
"Dramburg",
"Tempelburg",
"Angermünde",
"Strausberg",
"Liebenwalde",
"Wolmirstedt",
"Havelberg",
"Vorsfelde",
"Zossen",
"Spremberg"




```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
