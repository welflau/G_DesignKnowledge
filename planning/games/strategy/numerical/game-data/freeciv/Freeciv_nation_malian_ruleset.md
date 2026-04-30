# Freeciv(nation) · malian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/malian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的malian定义

## 正文
```ruleset
[nation_malian]

name=_("Malian")
plural=_("?plural:Malians")
groups="Modern", "African"
legend=_("Mali is a large country in Western Africa. Once part of French\
 Sudan, it gained independence together with Senegal in 1959.")

leaders = {
 "name",                "sex"
 "Aminata Traoré",      "Female"
 "Moussa Traoré",       "Male"
 "Modibo Keïta",        "Male"
 "Aoua Keïta",          "Female"
 "Ahmed Baba",          "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Monarchy",        _("Mansa %s"),        _("?female:Mansa %s")
}

flag="mali"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Mali"
civilwar_nations="Burkinabe", "Senegalese", "tuareg"

; City list based on http://de.wikipedia.org/wiki/Liste_der_Städte_in_Mali
cities =
 "Bamako",
 "Sikasso",
 "Mopti",
 "Koutiala",
 "Kayes",
 "Ségou",
 "Nioro du Sahel",
 "Niono",
 "Markala",
 "Kolondiéba",
 "Kati",
 "Gao",
 "Kolokani",
 "Ménaka",
 "Bougouni",
 "Niafunké",
 "Tombouctou",
 "Banamba",
 "Macina",
 "Nara",
 "Bafoulabé",
 "San",
 "Koulikoro",
 "Djenné",
 "Sokolo",
 "Yorosso",
 "Kangaba",
 "Kidal",
 "Diré",
 "Goundam",
 "Douentza",
 "Tenenkou",
 "Bandiagara",
 "Kimparana",
 "Kita",
 "Araouane",
 "Taoudenni",
 "Tessalit"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
