# Freeciv(nation) · centralafrican

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/centralafrican.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的centralafrican定义

## 正文
```ruleset
[nation_central_african]

name=_("Central African")
plural=_("?plural:Central Africans")
groups="Modern", "African"
legend=_("The Central African Republic is a country in Central Africa,\
 formerly known as the French African territory of Ubangi-Shari. It was\
 ruled briefly as a dictatorship in the 70s under Emperor Bokassa I during\
 which it was called the Central African Empire.")
leaders=
{
 "name",		"sex"
 "André Kolingba",	"male"
 "David Dacko",		"male"
 "Elisabeth Domitien",	"female"
 "Jean-Bédel Bokassa",	"male"
 "Barthélemy Boganda",	"male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Monarchy",        _("Emperor %s"),   _("Empress %s")
}

flag="car"
flag_alt="-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Chadian", "Congolese", "Cameroonian"

cities =
 "Bangui",
 "Bimbo",
 "Mbaiki",
 "Berbérati",
 "Kaga-Bandoro",
 "Bozoum",
 "Carnot",
 "Sibut",
 "Bambari",
 "Bria",
 "Bouar",
 "Bossangoa",
 "Nola",
 "Bangassou",
 "Damara",
 "Mobaye",
 "Paoua",
 "Boda",
 "Ippy",
 "Batangafo",
 "Alindao",
 "Kabo",
 "Rafaï",
 "Bouca",
 "Obo",
 "Ndélé",
 "Kembé",
 "Mongoumba",
 "Yakolé",
 "Birao",
 "Gamboula",
 "Kouango",
 "Baoro",
 "Boali",
 "Oudda",
 "Gambo",
 "Ouango"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
