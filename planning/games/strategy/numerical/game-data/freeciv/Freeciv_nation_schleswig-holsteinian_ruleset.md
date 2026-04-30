# Freeciv(nation) · schleswig-holsteinian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/schleswig-holsteinian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的schleswig-holsteinian定义

## 正文
```ruleset
[nation_schleswig-holsteinian]

name=_("Schleswig-Holsteinian")
plural=_("?plural:Schleswig-Holsteinians")
groups="European", "Medieval"
legend=_("For much of its history, the duchies of Schleswig and Holstein\
 have been contested by Germany and Denmark. The territories were united\
 in a personal union in 1375. In the 19th century, Schleswig-Holstein's\
 confused status led to two wars between Denmark and Prussia, and in 1866\
 Schleswig-Holstein became a Prussian province. After World War I, Northern\
 Schleswig was annexed by Denmark. Currently Schleswig-Holstein is a state\
 of the Federal Republic of Germany.")
leaders = {
 "name",		"sex"
"Mechthild",		"female"
"Heinrich der Eiserne",	"male"
"Gerhard III",		"male"
"Adolf IV",		"male"
"Johann der Jüngere",	"male"
"Karl Friedrich",	"male"
"Theodor Steltzer",	"male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("Duke %s"),         _("Duchess %s")
 "Fundamentalism",  _("Bishop %s"),       _("?female:Bishop %s")
 "Monarchy",        _("Grand Duke %s"),   _("Grand Duchess %s")
 "Democracy", _("Minister-President %s"), _("?female:Minister-President %s")
}

flag="schleswig-holstein" 
flag_alt = "-" 
style = "european" 

init_techs="" 
init_buildings="" 
init_units="" 

civilwar_nations = "oldenburgian", "danish", "frisian"

cities = 
"Schleswig",		;historical capital of Schleswig
"Kiel",			;capital of Holstein
"Flensburg",		;later capital of Schleswig
"Sonderburg",		;Danish Sønderborg
"Heide",
"Tondern",		;Danish Tønder
"Neumünster",
"Apenrade",		;Danish Aabenraa
"Plön",
"Oldenburg in Holstein",
"Itzehoe",
"Eckernförde",
"Husum",
"Bad Oldesloe",
"Hadersleben",		;Danish Haderslev
"Bordesholm",
"Bad Segeberg",
"Pinneberg",
"Rendsburg",
"Wyk auf Föhr (ocean)",
"Glückstadt",
"Burg auf Fehmarn (ocean)",
"Norburg",		;Danish Norborg
"Westerland (ocean)",
"Bargteheide",
"Meldorf",
"Christiansfeld",	;Danish Christiansfeld
"Brunsbüttel",
"Heiligenhafen",
"Neustadt in Holstein",
"Gravenstein",		;Danish Gråsten
"Kaltenkirchen",
"Marne",
"Norderstedt",
"Reinbek",
"Reinfeld",
"Tönning",
"Preetz",
"Schwentinental",
"Pattburg",		;Danish Padborg
"Bad Bramstedt",
"Wahlstedt",
"Tingleff",		;Danish Tinglev
"Bredstedt",
"Glinde",
"Wilster",
"Woyen",		;Danish Vojens
"Altona",
"Wandsbek",

;Free City of Lübeck, not historically part of Schleswig-Holstein
"Lübeck",

;Duchy of Saxe-Lauenburg
"Lauenburg/Elbe",
"Ratzeburg",
"Geesthacht"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
