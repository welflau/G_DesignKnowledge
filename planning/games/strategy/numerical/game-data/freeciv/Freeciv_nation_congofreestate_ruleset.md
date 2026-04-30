# Freeciv(nation) · congofreestate

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/congofreestate.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的congofreestate定义

## 正文
```ruleset
[nation_congofreestate]

name=_("Congo Free State")
plural=_("?plural:Congo Free States")
groups="Modern", "African"

legend=_("The Congo Free State was a large state in Central Africa from 1885 to 1908\
 which was in personal union with the Kingdom of Belgium under Leopold II.\
 Leopold's reign in the Congo eventually earned infamy due to the increasing\
 mistreatment of the indigenous people.")

leaders = {
 "name",                        "sex"
 "Leopold II",                  "Male"	
 "Marie Henriette",             "Female"
 "Francis Walter de Winton",    "Male"
 "Camille Janssen",             "Male"
 "Théophile Wahis",             "Male"
 "Joseph Conrad",               "Male"
 "Henry Morton Stanley",        "Male"
 "Tippu-Tip",                   "Male"
}

ruler_titles = {
 "government",      "male_title",                     "female_title"
 "Despotism",       _("Governeror-General %s"),      _("?female:Governeror-General %s")
}

flag = "congofreestate"
flag_alt = "dr_congo"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
conflicts_with = "kongo", "congolese"
civilwar_nations = "katangan", "rwandan", "burundian", "kongo", "congolese"

cities =
 "Léopoldville", 
 "Elisabethville",
 "Bakwanga",
 "Costermansville",
 "Luluabourg", 
 "Stanleyville", 
 "Tshikapa", 
 "Kolwezi", 
 "Jadotville",
 "Goma",
 "Kikwit", 
 "Uvira",
 "Bunia",
 "Coquilhatville", 
 "Matadi", 
 "Butembo", 
 "Kabinda", 
 "Mwene-Ditu", 
 "Paulis",
 "Boma",
 "Kindu",
 "Kamina", 
 "Ngandajika",
 "Banningville", 
 "Gemena", 
 "Kipushi",
 "Baraka",
 "Bumba",
 "Thysville",
 "Beni",
 "Albertville",
 "Moanda",
 "Tshilenge",
 "Lisala",
 "Kisantu", 
 "Bukama-Kibanda",
 "Port-Franqui",
 "Baudouinville",
 "Basoko-Bandu",
 "Kamisuku",
 "Mangaï",
 "Dibaya-Lubwe",
 "Mombombo",
 "Kikondja",
 "Sentery",
 "Luhatahata",
 "Kinzau-Vuete",
 "Kateba",
 "Luambo",
 "Bokungo"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
