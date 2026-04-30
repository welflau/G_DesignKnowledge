# Freeciv(nation) · tanzanian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/tanzanian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的tanzanian定义

## 正文
```ruleset
[nation_tanzanian]

name=_("Tanzanian")
plural=_("?plural:Tanzanians")
groups="African", "Modern"
legend=_("Tanzania was formed as a merger of the former British colonies\
 of Tanganyika and Zanzibar in 1964. For two decades the country was\
 ruled by Julius Nyerere, who followed the tenets of African socialism.\
 In 1985 Nyerere was the first African head of state to voluntarily step\
 down.")

leaders = {
 "name",                "sex"
 "Julius Nyerere",      "Male"
 "Edward Sokoine",      "Male"
 "Ali Hassan Mwinyi",   "Male"
}

flag="tanzania"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "tanganyikan", "zanzibari", "maasai"
conflicts_with = "tanganyikan", "zanzibari"

cities =
 "Dodoma (!ocean)",
 "Dar es Salaam (ocean)",
 "Zanzibar (ocean)",
 "Mwanza",
 "Arusha",
 "Mbeya",
 "Morogoro",
 "Tanga",
 "Kigoma",
 "Moshi",
 "Tabora",
 "Songea",
 "Musoma",
 "Shinyanga",
 "Chake Chake",
 "Katumba",
 "Iringa",
 "Ushirombo",
 "Mtwara",
 "Kilosa",
 "Sumbawanga",
 "Bagamoyo",
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
