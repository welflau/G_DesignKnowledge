# Freeciv(nation) · beninese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/beninese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的beninese定义

## 正文
```ruleset
[nation_beninese]

name=_("Beninese")
plural=_("?plural:Beninese")
groups="African", "Modern"
legend=_("Once the site of the Dahomey kingdom, the country was colonized\
 by France in the 19th century. Dahomey became independent in 1960.\
 Marxists seized power in 1972 and renamed the country Benin three years\
 later. Multiparty rule returned in 1990.")

leaders = {
 "name",                      "sex"
 "Maurice Kouandété",         "Male"
 "Hubert Maga",               "Male"
 "Justin Ahomadégbé-Tomêtin", "Male"
 "Mathieu Kérékou",           "Male"
}

flag="benin"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "dahomean"
civilwar_nations = "togolese", "burkinabe"

cities =
 "Cotonou",
 "Porto-Novo (ocean)",
 "Abomey",
 "Parakou",
 "Lokossa",
 "Ouidah",
 "Natitingou",
 "Djougou",
 "Aplahoué",
 "Savalou",
 "Kandi",
 "Pobé",
 "Abomey-Calavi",
 "Bohicon",
 "Savé",
 "Nikki",
 "Dogbo",
 "Malanville",
 "Cové",
 "Kérou",
 "Sakété",
 "Comé",
 "Bembéréké",
 "Bassila",
 "Banikoara",
 "Dassa",
 "Tchaourou",
 "Kétou",
 "Allada",
 "Tanguiété",
 "Aplahoué",
 "N'dali",
 "Bori",
 "Ségbana",
 "Beterou",
 "Athiémé",
 "Grand Popo",
 "Kouandé"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
