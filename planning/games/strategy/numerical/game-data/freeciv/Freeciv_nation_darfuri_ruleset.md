# Freeciv(nation) · darfuri

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/darfuri.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的darfuri定义

## 正文
```ruleset
[nation_darfuri]

name=_("Darfuri")
plural=_("?plural:Darfuris")
groups="Early Modern", "African"

legend=_("The Sultanate of Darfur was an eastern so-called Sahelian\
 state that from its location in the region just south of the\
 Sahara benefited and prospered from trans-Saharan trade. The region had\
 previously been dominated by the Daju and Tunjur ethnic groups, the\
 latter of which is traditionally thought to have introduced Islam to the\
 region. By the 16th century CE an ethnic group known as the Fur had\
 gained the upper hand and under Sultan Sulayman established a long-lasting\
 sultanate. The word Darfur means the Land of the Fur.")

leaders = {
 "name",                    "sex"
 "Abd-er-Rahman el-Rashid", "Male"
 "Mohammed Terab",          "Male"
 "Ahmed Bukr",              "Male"
 "Musa Sulayman",           "Male"
 "Sulayman Solong",         "Male"
 "Daali",                   "Male"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Monarchy",        _("Sultan %s"),         _("Sultana %s")
}

flag="darfur"
flag_alt="-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Sudanese", "Chadian", "Kanem-Bornu"

cities =
 "Al-Fashir",
 "Kobbei",
 "Ailliet",
 "Kebkabiya",
 "Kutum",
 "Mellit",
 "Tawilah",
 "Umm Kadadah",
 "Nyala",
 "Al-Junaynah", ; Geneina
 "Dar Masalit",
 "Miski",
 "El'Atrun",
 "Nukheila",
 "Ed Da'ein",
 "Tullus",
 "Buram",
 "Radom",
 "Kafia Kingi",
 "Meramta",
 "Garsilla",
 "Habar Banga",
 "Kas"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
