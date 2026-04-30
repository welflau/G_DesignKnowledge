# Freeciv(nation) · peruvian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/peruvian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的peruvian定义

## 正文
```ruleset
[nation_peruvian]

name=_("Peruvian")
plural=_("?plural:Peruvians")
groups="Modern", "American"
legend=_("Peru was the cradle of the Inca Empire and civilization. It is\
 still today a major center of indigenous South American culture.")

leaders = {
 "name",                        "sex"
 "Andrés de Santa Cruz",        "Male"
 "Agustín Gamarra",             "Male"
 "Ramón Castilla",              "Male"
 "Andrés Avelino Cáceres",      "Male"
 "José Pardo y Barreda",        "Male"
 "Augusto B. Leguía",           "Male"
 "Manuel A. Odría",             "Male"
 "Fernando Belaúnde Terry",     "Male"
 "Alberto Fujimori",            "Male"
}

ruler_titles = {
 "government",      "male_title",             "female_title"
 "Communism",       _("Comandante %s"),       _("Comandanta %s")
 "Despotism",       _("Protector %s"),        _("?female:Protector %s")
 "Monarchy",        _("Viceroy %s"),          _("Vicereine %s")
 "Fundamentalism",  _("Archbishop %s"),       _("Mother Superior %s")
}

flag="peru"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "inca"
civilwar_nations = "chilean", "inca", "bolivian"

cities =
 "Lima",
 "Arequipa",
 "Piura",
 "Trujillo",
 "El Callao (ocean)",
 "Chiclayo (ocean)",
 "Huancayo",
 "Chimbote (ocean)",
 "Iquitos",
 "Cusco",
 "Ica",
 "Tacna",
 "Pucallpa",
 "Juliaca",
 "Huánuco",
 "Sullana",
 "Ayacucho",
 "Cajamarca",
 "Talara",
 "Puno",
 "Tumbes"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
