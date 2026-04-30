# Freeciv(nation) · argentine

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/argentine.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的argentine定义

## 正文
```ruleset
[nation_argentine]

name=_("Argentine")
plural=_("?plural:Argentines")
groups="Modern", "American"
legend=_("Argentina is located on the south-eastern coast of South America.\
 Since independence from Spain in 1816, it has been plagued by several\
 internal and external conflicts. In the decades after World War II, the\
 country's politics was dominated by Juan Perón and his charismatic wife Eva\
 \"Evita\" Perón.")

leaders = {
 "name",                        "sex"
 "José de San Martín",          "Male"
 "Juan Manuel de Rosas",        "Male"
 "Justo Urquiza",               "Male"
 "Bernardino Rivadavia",        "Male"
 "Domingo Sarmiento",           "Male"
 "Juan Domingo Perón",          "Male"
 "Eva Duarte de Perón",         "Female"
}

ruler_titles = {
 "government",     "male_title",        "female_title"
 "Communism",      _("Comandante %s"),  _("Comandanta %s")
 "Despotism",      _("Caudillo %s"),    _("Caudilla %s")
 "Fundamentalism", _("Cardinal %s"),    _("Mother Superior %s")
 "Monarchy",       _("Viceroy %s"),     _("Vicereine %s")
}

flag="argentina"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "paraguayan", "uruguayan", "mapuche"

cities =
 "Buenos Aires",
 "Mar del Plata (ocean)",
 "Rosario",
 "La Plata",
 "Paraná",
 "Santa Fe",
 "Corrientes (river)",
 "Resistencia",
 "Salta",
 "Córdoba",
 "San Miguel de Tucumán",
 "Santiago del Estero (swamp, !mountains)",
 "San Juan",
 "Mendoza",
 "Bahía Blanca (ocean)",
 "San Salvador de Jujuy",
 "Formosa",
 "Catamarca",
 "San Luis",
 "Río Cuarto (river)",
 "Villa María",
 "San Nicolás de los arroyos (river)",
 "Zárate",
 "Junín",
 "Comodoro Rivadavia",
 "San Carlos de Bariloche",
 "Tandil",
 "Tartagal",
 "Embarcación (river)",
 "Libertador General San Martín",
 "San Antonio de los Cobres",
 "Metán",
 "Rosario de la Frontera",
 "Las Lomitas",
 "Campo Gallo",
 "Tintina",
 "Andalgalá",
 "Tinogasta",
 "Añatuya",
 "Pinto",
 "Tostado",
 "Santo Tomé",
 "Mercedes",
 "Albardón",
 "Quilmes",
 "San Rafael",
 "General Alvear",
 "Malargüe",
 "Zapala",
 "Neuquén",
 "General Roca",
 "Venado Tuerto",
 "Rufino",
 "Pergamino",
 "Ibicuy",
 "Maipú",
 "Chascomús",
 "Dolores",
 "Las Flores",
 "Balcarce",
 "Necochea",
 "25 de Mayo",
 "9 de Julio",
 "Olavarría",
 "Coronel Suárez",
 "Coronel Pringles",
 "Tres Arroyos (river)",
 "Punta Alta", 
 "General Acha",
 "Río Colorado (river)",
 "San Cristóbal",
 "Santa Isabel",
 "Pehuajo",
 "Viedma",
 "Maquinchao",
 "Esquel",
 "Paso de indios",
 "Las Plumas",
 "Rawson",
 "Sarmiento",
 "San Julián",
 "Perito Moreno",
 "Puerto Deseado (ocean)",
 "Santa Cruz",
 "Río Gallegos (river)",
 "Río Grande (river)",
 "Ushuaia",
 "Entre Ríos (river)",
 "Chimbas",
 "El Leoncito",
 "Lanús",
 "Morón",
 "San Lorenzo",
 "Teniente Matienzo",
 "Cruz del Eje",
 "San Pedro",
 "Río Negro (river)",
 "Quequén",
 "Decepción",
 "Esperanza"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
