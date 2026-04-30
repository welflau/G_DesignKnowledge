# Freeciv(nation) · castilian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/castilian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的castilian定义

## 正文
```ruleset
[nation_castilian]

name=_("Castilian")
plural=_("?plural:Castilians")
groups="European", "Medieval"
legend=_("Castile emerged to become the most powerful of the medieval\
 Spanish kingdoms. It absorbed Leon and later formed a personal union\
 with Aragon. Its current territory is divided over several autonomous\
 communities of Spain.")

leaders = {
 "name",                        "sex"
 "Fernando Aznárez",            "Male"
 "Fernando el Grande",          "Male"
 "Sancho el Fuerte",            "Male"
 "Alfonso el Bravo",            "Male"
 "Rodrigo Díaz de Vivar",       "Male"
 "Urraca I",                    "Female"
 "Alfonso, el de Las Navas",    "Male"
 "Fernando el Santo",           "Male"
 "Alfonso el Sabio",            "Male"
 "Sancho el Bravo",             "Male"
 "Enrique el Doliente",         "Male"
 "Isabel la Católica",          "Female"
 "Juana la Loca",               "Female"
 "Juan de Padilla",             "Male"
}

ruler_titles = {
 "government",     "male_title",     "female_title"
 "Despotism",      _("Count %s"),    _("Countess %s")
 "Fundamentalism", _("Cardinal %s"), _("Mother Superior %s")
}

flag="castile"
flag_alt = "spain"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="leonese", "aragonese"

cities =
 "Burgos",
 "Toledo",
 "Valladolid",
 "Madrid",
 "Alcalá de Henares",
 "Santander (ocean)",
 "Logroño",
 "Albacete",
 "Alcobendas",
 "Móstoles",
 "Talavera de la Reina",
 "Palencia",
 "Fuenlabrada",
 "Leganés",
 "Guadalajara (river)",
 "Ciudad Real",
 "Alcorcón",
 "Getafe",
 "Torrelavega",
 "Ávila",
 "Segovia",
 "Torrejón de Ardoz",
 "Cuenca (mountains, hills)",
 "Aranjuez",
 "Parla",
 "Puertollano",
 "Tomelloso",
 "Soria",
 "Miranda de Ebro (river)",
 "Camargo",
 "Aranda de Duero (river)",
 "Alcázar de San Juan",
 "Azuqueca de Henares",
 "Hellín",
 "Valdepeñas",
 "Vilarrobledo",
 "Almansa",
 "Camargo (ocean)",
 "Calahorra",
 "Medina del Campo",
 "Requena",
 "San Lorenzo",
 "El Escorial",
 "Béjar",
 "Guadarrama",
 "Los Corrales de Buelna",
 "Tordesillas",
 "Las Navas de Tolosa",
 "Villalar",
 "Vivar"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
