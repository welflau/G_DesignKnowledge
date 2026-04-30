# Freeciv(nation) · suebian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/suebian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的suebian定义

## 正文
```ruleset
[nation_suebian]

name=_("Suebian")
plural=_("?plural:Suebians")
groups="Ancient", "Medieval", "European"
legend=_("The Suebians were an ancient West Germanic tribal confederation,\
 which may have been formed by Ariovistus for his expedition to Gaul.\
 The Suebians included the Germanic tribes from the Elbe river basin\
 belonging to the Herminonic language group, such as the Marcomanni and\
 Quadi. Between the first and fourth centuries CE they were a threat to\
 Rome, often encroaching on the Danube provinces of the empire. In 405-406\
 CE the Suebians were forced to leave their lands by the Huns and during\
 New Year's night in 405 CE they crossed the frozen Rhine together with\
 the Vandals and the Alans. They settled in the northwest of the Iberian\
 Peninsula, where they established their own kingdom, which was conquered\
 by the Visigoths in 585 CE.")
leaders = {
 "name",                "sex"
 "Ariovistus",          "Male"        ;probably a suebian chieftain, known in
                                      ;sources as a Rex Germanorum
 "Marobodwus",          "Male"        ;Marbod
 ;Suebian kings in Hispania:
 "Hermenerik",          "Male"        ;Hermeric
 "Harjamigarjas",       "Male"        ;Heremigarius
 "Rexwila",             "Male"        ;Rechila
 "Rexjar",              "Male"        ;Rechiar
 "Ajulf",               "Male"        ;Aiulf
 "Maldras",             "Male"
 "Framta",              "Male"
 "Reximund",            "Male"        ;Rechimund
 "Frumar",              "Male"
 "Remismund",           "Male"
 "Weremund",            "Male"
 "Theudemund",          "Male"
 "Xararik",             "Male"
 "Arjamir",             "Male"
 "Theudemir",           "Male"
 "Miro",                "Male"
 "Eborik",              "Male"
 "Andeka",              "Male"
 "Malarik",             "Male"
}
flag="suebian"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="spanish", "portuguese", "galician", "asturian", "german",
 "czech", "east german", "thuringian"
civilwar_nations = "Visigothic", "Western Roman"

cities =
 "Bracara Augusta",	;Braga
 "Portus Cale",		;Porto
 "Lucus Augusti",	;Lugo
 "Asturica Augusta",	;Astorga
 "Corunium",		;A Coruña
 "Campus Stellae",	;Santiago de Compostela
 "Conimbriga",		;Coimbra
 "Vicus",		;Vigo
 "Brigantia",		;Bragança
 "Legio",		;León
 "Aquae Urentes",	;Ourense
 "Lamecum",		;Lamego
 "Flavium Brigantium",	;Betanzos
 "Iria Flavia",		;Padrón
 "Tude",		;Tui
 "Pons Veteris",	;Pontevedra
 "Britonia",
 "Viso",		;Viseu
 "Nemetobriga",
 "Aquae Flaviae",	;Chaves
 "Aegitania",		;Idanha
 "Aquae Querquennae",
 "Dactonium",		;Monforte de Lemos
 "Lamaecus",		;Lamego
 "Sabaria",
 "Forum Limicorum",	;Ginzo de Limia
 "Villa Alba",		;Vilalba
 "Querculus",		;O Carballiño
 "Libunca"		;Ribadeo

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
