# Freeciv(nation) · vandalic

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/vandalic.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的vandalic定义

## 正文
```ruleset
[nation_vandalic]

name=_("Vandalic")
plural=_("?plural:Vandals")
groups="Ancient", "Medieval", "European", "African"
legend=_("The Vandals were an East Germanic people originating from what\
 is now Southern Poland and Slovakia. They entered the Roman Empire in\
 the early 5th century CE. Led by Geiseric, they eventually founded a\
 kingdom in Carthage. The Vandals are perhaps best known for their sack\
 of Rome in 455 CE. In 534 CE Belisarius conquered the Vandalic kingdom\
 for the Byzantine Empire.")

leaders = {
 "name",        "sex"
 "Wisimar",     "Male"
 "Godigisel",   "Male"
 "Gundereiks",  "Male"
 "Gensereiks",  "Male"
 "Hunereiks",   "Male"
 "Gunþamund",   "Male"
 "Þrasamund",   "Male"
 "Hildereiks",  "Male"
 "Geilamir",    "Male"
}

ruler_titles = {
 "government",        "male_title",       "female_title"
 "Fundamentalism",    _("Presbyter %s"),  _("?female:Presbyter %s") 
 "Anarchy",           _("Usurper %s"),    _("?female:Usurper %s") 
 "Republic",          _("Consul %s"),     _("?female:Consul %s") 
}

flag="vandal"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""
conflicts_with = "polish", "slovakian", "carthaginian", "tunisian"
civilwar_nations = "visigothic", "amazigh", "ostrogothic", "suebian"

cities =
 "Carthago",		;Carthage
 "Sitiphis",		;Sétif
 "Caralis",		;Cagliari
 "Saldae",		;Béjaïa
 "Syracusae",		;Syracusa
 "Alalia",		;Aléria
 "Caesarea",		;Cherchell
 "Constantina",		;Cirta
 "Panormus",		;Palermo
 "Tingis",		;Tanger
 "Thapsus",
 "Thevestis",		;Tebessa
 "Tacape",		;Gabès
 "Lixus",
 "Palma",		;Palma de Mallorca
 "Leptis Magna",
 "Volubilis",		;Walili
 "Hadrumetum",		;Sousse
 "Turris",		;Porto Torres
 "Hippo Diarrhytus",	;Bizerte
 "Hippo Regius",	;Annaba
 "Messena",		;Messina
 "Capsa",		;Gafsa
 "Tripolis",		;Tripoli
 "Pollentia",		;Pollença
 "Utica",
 "Ruspe",		;Thélepte
 "Lilybaeum",		;Marsala
 "Icosium",
 "Thamugadi",		;Timgad
 "Bulla Regia",
 "Thugga",		;Dougga
 "Portus Magonis", 	;Maó
 "Thysdrus",		;El Djem
 "Leptiminus",		;Lamta
 "Agrigentum",		;Agrigento
 "Thuburbo Maius",
 "Ruspina",		;Monastir
 "Ebusus",		;Eivissa
 "Leptis Parva",
 "Segesta",		;Segesta
 "Ad Decimum",
 "Tricamarum"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
