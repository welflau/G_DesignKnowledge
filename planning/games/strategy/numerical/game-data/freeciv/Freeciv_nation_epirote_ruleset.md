# Freeciv(nation) · epirote

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/epirote.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的epirote定义

## 正文
```ruleset
[nation_epirote] 

name=_("Epirote") 
plural=_("?plural:Epirotes") 
groups="Ancient", "European" 
legend=_("The Epirotes were the ancient inhabitants of the Epirus region\
 in northwestern Greece. Their most powerful ruler Pyrrhus launched a\
 campaign against Rome in Italy, which ended in the famous \"Pyrrhic\
 Victory\".")
leaders= {
"name",                "sex"
"Pyrrhos",             "Male"
"Arrybas",             "Male"
"Alkon",               "Male"
"Neoptolemos",         "Male"
"Admetos",             "Male"
"Aiakides",            "Male"
"Falakrion",           "Male"
"Deinon",              "Male"
"Zopyros",             "Male"
"Kallikrates",         "Male"
}
flag= "epirus" 
flag_alt = "greece" 
style = "Classical" 

ruler_titles = { "government", "male_title",     "female_title"
                 "Anarchy",    _("Usurper %s"),  _("?female:Usurper %s")
                 "Democracy",  _("Speaker %s"),  _("?female:Speaker %s") 
                 "Despotism",  _("Tyrant %s"),   _("?female:Tyrant %s")
}

init_techs="" 
init_buildings="" 
init_units="" 

conflicts_with="albanian"
civilwar_nations="macedon", "italian greek", "illyrian"

cities =
  "Dodona",
  "Passaron",
  "Euroia",
  "Arta",
  "Ephyra",
  "Nikopolis",
  "Phoinika",
  "Thesproteia",
  "Artikheia",
  "Berenike",
  "Kreonion",
  "Palaiste",
  "Khimaira",
  "Maiandria",
  "Panormos",
  "Kharadros",
  "Onkhesmos",
  "Antigoneia",
  "Phanotes",
  "Eurymenai",
  "Ambrakia",
  "Bouthroton",
  "Antipatreia",
  "Pelion",
  "Aulon",
  "Baiake",
  "Kestrine",
  "Gertus",
  "Hekatompedon",
  "Photiki",
  "Orikos",
  "Thronion",
  "Orraon",
  "Bouneima",
  "Tekmona",
  "Gitanai",
  "Kassopa",
  "Elateia",
  "Batiai",
  "Helikranon",
  "Elina",
  "Sybota",
  "Kheimerion",
  "Toryne",
  "Elatreia",
  "Poionos"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
