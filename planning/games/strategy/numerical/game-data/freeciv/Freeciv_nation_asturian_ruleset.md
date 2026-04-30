# Freeciv(nation) · asturian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/asturian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的asturian定义

## 正文
```ruleset
[nation_asturian]

name=_("Asturian")
plural=_("?plural:Asturians")
groups="Ancient", "European"
legend=_("The Astures were a Celtic people which occupied most of the northern\
 coast of Spain. They battled against the Roman Empire until their defeat by\
 Caesar Augustus' legions between 29 and 19 BCE. Under the Visigothic kingdom of\
 Toledo, there were uneasy relations between Visigoths and Asturians. In 722 CE,\
 king Pelayo defeated the Umayyad Muslim troops at Covadonga, establishing\
 the Asturian Kingdom, which lasted until 910 CE, when the capital town was\
 moved from Oviedo to Leon. Nowadays, Asturias is an autonomous community of\
 Spain.")

leaders = {
 "name",                        "sex"
 "Pelayo",                      "Male"
 "Alfonso II",                  "Male"
 "Ramiro I",                    "Male"
 "Favila I",                    "Male"
 "Gonzalo Peláez",              "Male"
 "Xosefa de Xovellanos",        "Female"
 "Aida Lafuente",               "Female"
 "Rosario Acuña",               "Female"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Despotism",       _("Prince %s"),         _("Princess %s")
 "Fundamentalism",  _("Bishop %s"),         _("Mother Superior %s")
}

flag="asturias"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""
conflicts_with="spanish"
civilwar_nations="galician", "basque", "gallic", "leonese"

cities =
  "Xixón", "Uviéu", "Avilés", "Cangues d'Onís", "La Pola Siero", "Grau",
  "Cangas", "Ribesella", "Mieres", "Llugones", "Llangréu", "A Veiga",
  "Villaviciosa", "Candás", "Cuideiru", "Les Arriondes", "Lluanco",
  "Llanes", "L.luarca", "Navia", "Pravia", "Tapia", "La Vega", 
  "La Puela", "Nubleo", "Muros", "Nava", "Soto Ribera", "Posada",
  "Prau", "Martimporra", "Grullos", "Colunga", "Llastres", "Sames",
  "Les Arenes", "Santolaya de Morcín", "Benia", "Tinéu", "Salas",
  "Bual", "El Campu", "Castropol", "Villabre", "Santalla d'Ozcos",
  "Samartín", "Eilao", "Panes", "Colombres", "Cabanaquinta", "Cuadonga",
  "Balmonte", "Vilanova", "Degaña", "Alles", "Taramundi", "Noreña",
  "La Plaza", "San Xuan de Beleño", "Villayón", "Bárzana", "Grandas",
  "Santuyanu", "Santantolín", "La Caizuela", "Proaza", "Villanueva",
  "Santolaya de Cabranes", "Cuaña", "La Pola Somiedu", "Pezós", 
  "L'Infiestu", "Vega", "Rusecu", "A Caridá", "O Chao"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
