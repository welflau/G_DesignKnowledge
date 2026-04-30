# Freeciv(nation) · tanganyikan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/tanganyikan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的tanganyikan定义

## 正文
```ruleset
[nation_tanganyikan]

name=_("Tanganyikan")
plural=_("?plural:Tanganyikans")
groups="African"
legend=_("Inhabited by Bantu tribes since the beginning of the Common Era,\
 Tanganyika became a German colony in the late 19th century. It was\
 conquered by the British during World War I and declared independence in\
 1961. Three years later it merged with Zanzibar to form the Union of\
 Tanzania.")

leaders = {
 "name",                         "sex"
 "Paul Emil von Lettow-Vorbeck", "Male"
 "Horace Byatt",                 "Male"
 "Richard Gordon Turnbull",      "Male"
 "Julius Nyerere",               "Male"
 "Rashidi Kawawa",               "Male"
}

flag="tanganyika"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "maasai", "swahili"

cities =
 "Dar es Salaam (ocean)",
 "Bagamoyo",
 "Mwanza",
 "Arusha",
 "Mbeya",
 "Morogoro",
 "Dodoma",
 "Tanga",
 "Kigoma",
 "Moshi",
 "Tabora",
 "Songea",
 "Musoma",
 "Shinyanga",
 "Katumba",
 "Iringa",
 "Ushirombo",
 "Mtwara",
 "Kilosa",
 "Sumbawanga",
 "Mpanda",
 "Bukoba",
 "Singida",
 "Uyovu",
 "Sengerama",
 "Kalangalala",
 "Mishoma",
 "Mererani",
 "Buseresere",
 "Bunda",
 "Makambako",
 "Katoro",
 "Ifakara",
 "Njombe",
 "Utengule Usongwe",
 "Kiranyi",
 "Siha Kati",
 "Nkome",
 "Nkololo",
 "Nguruka",
 "Lindi",
 "Vwawa"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
