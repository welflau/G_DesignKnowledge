# Freeciv(nation) · leonese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/leonese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的leonese定义

## 正文
```ruleset
[nation_leonese]

name=_("Leonese")
plural=_("?plural:Leonese")
groups="European", "Medieval"
legend=_("Leon was a medieval kingdom in the northwestern part of the\
 Iberian peninsula. Currently Leon is part of the Spanish autonomous\
 community of Castile and Leon.")

leaders = {
 "name",                        "sex"
 "García I",                    "Male"
 "Fruela II",                   "Male"
 "Alfonsu VII",                 "Male"
 "Fernandu II",                 "Male"
 "Alfonsu IX de Borgoña",       "Male"
 "José Eguiagaray",             "Male"
}

ruler_titles = {
 "government",     "male_title",   "female_title"
 "Fundamentalism", _("Bishop %s"), _("Mother Superior %s")
}

flag="leon"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="asturian", "galician", "castilian"

cities =
 "Llión",
 "Salamanca",
 "Zamora",
 "Ponferrada",
 "Sanandrés del Rabanéu",
 "Benavente",
 "Villaquilame",
 "Santa Marta de Tormes",
 "Béyar",
 "Ciá Rodrigu",
 "Astorga",
 "La Bañeza",
 "Vitsablinu",
 "Bembibre",
 "Toru",
 "Villamayor",
 "Valverde de la Virgen",
 "Peñaranda de Bracamonte",
 "Gixuelu",
 "Alba de Tormes",
 "Villares de la Reina",
 "Carbayosa de la Sagrada",
 "Cacabiellos",
 "Fabeiru",
 "La Robla",
 "Valencia de Don Xuan",
 "Campunaraya",
 "Sariegos",
 "Torenu",
 "La Pola de Gordón",
 "Cabreirizos",
 "Carracediellu",
 "Villafranca d'El Bierzu",
 "Terradiellos",
 "Cistierna",
 "Santa María del Páramu",
 "Villareyu d'Órbigu",
 "Torre d'El Bierzu",
 "Safagún",
 "Banavices",
 "Vitigudinu",
 "Torre de Santamarina",
 "Carrizu",
 "Veiga d'Espinareda",
 "Morales del Vinu",
 "Xouzas d'Abaixu",
 "Santa Marina del Rei",
 "Boñare",
 "Toural de los Vados",
 "San Xustu de la Veiga",
 "Valdeiras",
 "Valdefreisnu"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
