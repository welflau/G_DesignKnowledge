# Freeciv(nation) · prussian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/prussian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的prussian定义

## 正文
```ruleset
[nation_prussian]

name=_("Prussian")
plural=_("?plural:Prussians")
groups="Early Modern", "European"

legend=_("Prussia was originally the name of a pagan Baltic people, who in\
 the 13th century were conquered by the German Teutonic Knight order. The\
 knights established an independent state in this land, and in 1561 Grand\
 Master Albrecht I proclaimed himself hereditary Duke of Prussia. Evolving\
 into a regional military powerhouse, Prussia played an important role in\
 uniting the German nation in 1871 and solidified its power during the\
 Franco-Prussian war of the same year.")

leaders = {
 "name",                "sex"
 "Waldemar",            "Male"
 "Albrecht I",          "Male"
 "Albrecht Friedrich",  "Male"
 "Friedrich Wilhelm",   "Male"
 "Friedrich I",         "Male"
 "Otto von Bismarck",   "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",      _("Duke %s"),          _("Duchess %s")
 "Democracy",      _("Chancellor %s"),    _("?female:Chancellor %s")
 "Fundamentalism", _("Archbishop %s"),    _("?female:Archbishop %s")
 "Communism",      _("First Secretary %s"),_("?female:First Secretary %s")
}

flag         = "prussia"
flag_alt     = "-"
style        = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "german", "polish", "lithuanian", "brandenburgian"

; Sources:
; http://commons.wikimedia.org/wiki/Image:Rzeczpospolita_Royal_Ducal.png
; http://commons.wikimedia.org/wiki/Image:East_Prussia_1939.JPG

cities =
; Site of the first Teutonic castle in Prussia
 "Tapiau",
; Royal Prussia
 "Elbing",
 "Marienburg",
 "Danzig",
 "Dirschau",
 "Frauenburg",
 "Putzig",
 "Konitz",
 "Graudenz",
 "Kulm",
 "Thorn",
 "Heilsberg",
 "Allenstein",
; Ducal Prussia
 "Königsberg",
 "Braunsberg",
 "Marienwerder",
 "Wehlau",
 "Tilsit",
 "Lyck",
 "Memelburg",
; Late East Prussia
 "Stettin",
 "Pillau",
 "Eylau",
 "Osterode",
 "Rastenburg",
 "Ortelsburg",
 "Angerburg",
 "Insterburg",
 "Goldap",
 "Gumbinnen",
; Brandenburg-Prussia
 "Berlin",
 "Potsdam",
 "Posen",
 "Frankfurt/Oder",
 "Cottbus",
 "Brandenburg an der Havel",
 "Charlottenburg",
 "Halle/Saale",
 "Küstrin",
; Later additions
 "Breslau",
 "Magdeburg",
 "Münster",
 "Köln",
 "Koblenz",
 "Kleve",
 "Sigmaringen",
 "Schneidemühl",
 "Oppeln",
 "Essen",
 "Düsseldorf",
 "Dortmund",
 "Greifswald",
 "Grünberg",
 "Trier",
 "Emden",
 "Bromberg",
 "Kiel",
 "Kassel",
 "Hannover",
 "Frankfurt am Main",
 "Wiesbaden",
 "Schleswig",
; Additions after German unification
 "Ratzeburg",
 "Arolsen"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
