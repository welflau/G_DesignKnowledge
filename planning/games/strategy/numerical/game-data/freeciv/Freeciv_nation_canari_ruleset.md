# Freeciv(nation) · canari

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/canari.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的canari定义

## 正文
```ruleset
[nation_canari]

name=_("Cañari")
; pre-2.6 had plain ASCII names
rule_name="Canari"
plural=_("?plural:Cañaris")
groups="Medieval", "American"
legend=_("The Cañaris were a pre-Columbian civilization in what is now\
 Ecuador, whose existence can be traced from the 6th century onwards.\
 They were one of the few Andean cultures not to worship the sun. The\
 Cañari language was probably related to the Mochica language of Peru,\
 but by the time of the Spanish conquest the Cañaris had mostly switched\
 to Quechua. The Cañaris formed a loose confederation with their main\
 political center in Guapdondelig, currently the city of Cuenca, capital\
 of the province of Azuay. They were subjugated by the Incas in the late\
 15th century, though they put up a fierce resistance. They rebelled during\
 the Incan civil war and sided with the Spanish during their conquest of\
 the Inca empire.")

leaders = {
 "name",        "sex"
 "Tenemaza",    "Male"
 "Carchipulla", "Male"
 "Duma",        "Male"
}

ruler_titles = {
 "government", "male_title",      "female_title"
 "Monarchy",   _("High King %s"), _("High Queen %s")
}

flag="canar"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""
conflicts_with = "ecuadorian"
civilwar_nations = "tairona", "chimu", "inca"

cities =
 "Guapdondelig",	;Tomebamba/Cuenca
 "Hatun Cañari",	;Ingapirca
 "Chobshi",
 "Yacubiñay",
 "Shabalula",
 "Coyoctor",
 "Culebrillas",
 "Alausi",
 "Guasunos",
 "Labrascarumi",
 "Sigsig",
 "Tarqui",
 "Dumapara",
 "Milchichig",
 "Chordeleg",
 "Peleusis",
 "Molleturo",
 "Gualaquiza",
 "Sinincay",
 "Pushio",
 "Saractar",
 "Nulti",
 "Mishquiaco",
 "Deleg",
 "Garmushi",
 "Percadil",
 "Susudel",
 "Churugusho",
 "Lentag",
 "Suscal",
 "Patadeli",
 "Chunasana",
 "Dircay",
 "Parig",
 "Pindilig",
 "Pichilcay",
 "Daligshi",
 "Molobog",
 "Shurun"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
