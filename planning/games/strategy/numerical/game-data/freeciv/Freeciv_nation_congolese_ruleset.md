# Freeciv(nation) · congolese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/congolese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的congolese定义

## 正文
```ruleset
[nation_congolese]

name=_("Congolese")
plural=_("?plural:Congolese")
groups="Modern", "African"

legend=_("The Democratic Republic of the Congo is a big country in\
 Central Africa. Despite (or because of) its wealth of natural\
 resources it has been in ruins for most of its modern history. In 1885\
 Congo was awarded to Léopold II of Belgium as his personal possession,\
 the Congo Free State, which turned the country into a slaughterhouse.\
 At least twenty per cent of the population perished and after an\
 international outcry it became a Belgian colony in 1906.\
 It achieved independence in 1960. The Mobutu dictatorship started\
 a new round of pillaging. When Mobutu was toppled the country sank\
 into a civil war, causing five million deaths, the bloodiest event\
 since World War II.")

leaders = {
 "name",                        "sex"
 "Léopold II de Belgique",      "Male"
 "Patrice Lumumba",             "Male"
 "Joseph Kasavubu",             "Male"
 "Mobutu Sese Seko",            "Male"
 "Laurent-Désiré Kabila",       "Male"
 "Joseph Kabila",               "Male"
}

flag="dr_congo"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
conflicts_with = "kongo"
civilwar_nations = "katangan", "rwandan", "burundian", "congofreestate"

cities =
 "Kinshasa (river)",
 "Lumumbashi (jungle)",
 "Kolwezi (river, jungle)",
 "Mbuyi-Mayi",
 "Kisangani",
 "Kananga",
 "Likasi",
 "Boma",
 "Tshikapa",
 "Bukavu",
 "Mewene-Ditu",
 "Kikwit",
 "Mbandaka",
 "Matadi (ocean)",
 "Uvira",
 "Gandajika",
 "Butembo",
 "Kalemie",
 "Goma (hills)",
 "Kindu",
 "Isiro",
 "Bandundu",
 "Gemena",
 "Ilebo",
 "Bumba",
 "Bunia",
 "Beni",
 "Mbanza-Ngungu",
 "Kamina",
 "Lisala",
 "Lodja",
 "Kipushi",
 "Kabinda",
 "Binga",
 "Kasongo",
 "Kalima",
 "Mweka",
 "Gbadolite",
 "Banana (ocean)",
 "Bulungu",
 "Lubao",
 "Buta",
 "Lusambo",
 "Basoko"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
