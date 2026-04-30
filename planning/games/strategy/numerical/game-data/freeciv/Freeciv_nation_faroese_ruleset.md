# Freeciv(nation) · faroese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/faroese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的faroese定义

## 正文
```ruleset
[nation_faroese]

name=_("Faroese")
plural=_("?plural:Faroese")
groups="European"
legend=_("The Faroe Islands are an archipelago in the Northern Atlantic\
 ocean. According to the sagas, they were first settled by Norsemen who\
 fled the tyranny of Norway's king Harald Fairhair. The islands became\
 a Norwegian possession in 1035 and passed to Denmark in 1814. The Faroes\
 have home rule since 1948.")

leaders = {
 "name",                        "sex"
 "Grímur Kamban",               "Male"
 "Leivur Øssursson",            "Male"
 "Turið Torkilsdóttir",         "Female"
 "Tróndur í Gøtu",              "Male"
 "Sigmundur Brestisson",        "Male"
 "Magnus Heinason",             "Male"
 "Nólsoyar Páll",               "Male"
 "Rasmus Christoffer Effersøe", "Male"
 "Jóannes Patursson",           "Male"
 "Helena Patursson",            "Female"
 "Atli P. Dam",                 "Male"
 "Marita Petersen",             "Female"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Democracy",       _("Speaker %s"),   _("?female:Speaker %s")
 "Despotism",       _("Earl %s"),      _("?female:Earl %s")
 "Fundamentalism",  _("Vicar %s"),     _("?female:Vicar %s")
}

flag="faroes"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "icelandic"

cities =
 "Tórshavn",
 "Kirkjubøur",
 "Klaksvík",
 "Fuglafjørður",
 "Vágur",
 "Miðvágur",
 "Sandur",
 "Runavík",
 "Leirvík",	;Eystur
 "Tvøroyri",
 "Sunda",
 "Nes",
 "Vestmanna",
 "Norðskáli",	;Sunda
 "Sørvágur",
 "Strendur",	;Sjóvar
 "Hvalba",
 "Eiði",
 "Kvívík",
 "Sandur",
 "Skopun",
 "Hvannasund",
 "Sumba",
 "Viðareiði",
 "Porkeri",
 "Skálavík",
 "Kunoy",
 "Húsavík",
 "Hov",
 "Fámjin",
 "Húsar",
 "Skúvoy",
 "Kirkja",	;Fugloy
 "Hoyvík",
 "Argir",
 "Funningur",
 "Gøtu",
 "Miðvágur",
 "Sandavágur",
 "Svínoy",
 "Elduvík",
 "Oyndarfjørð",
 "Skála",
 "Gjáar",
 "Haldarsvík",
 "Hósvík",
 "Hvalvík",
 "Saksun",
 "Hestur",
 "Nólsov",
 "Mikladalur",
 "Mykines",
 "Argja",
 "Kaldbaks",
 "Miðvágur",
 "Toftir"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
