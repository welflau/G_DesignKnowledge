# Freeciv(nation) · malagasy

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/malagasy.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的malagasy定义

## 正文
```ruleset
[nation_malagasy]

name=_("Malagasy")
plural=_("?plural:Malagasies")
groups="Medieval", "Modern", "African"
legend=_("The Malagasy are the people of Madagascar. For centuries, tribes\
 from Indonesia, East Africa and the Arab world have gathered on the\
 island.")

leaders = {
 "name",                "sex"
 "Radama I",            "Male"
 "Ranavalona I",        "Female"
 "Rasoherina",          "Female"
 "Ranavalona II",       "Female"
 "Rainilaiarivony",     "Male"
 "Didier Ratsiraka",    "Male"
}

ruler_titles = {
 "government", "male_title",              "female_title"
 "Republic",   _("High Commissioner %s"), _("?female:High Commissioner %s")
}

flag="madagascar"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="indonesian", "mauritian", "comorian"

; City list based on data from this page:
; http://de.wikipedia.org/wiki/Liste_der_Städte_in_Madagaskar
cities =
 "Antananarivo (!ocean)",
 "Toamasina",
 "Antsirabe",
 "Fianarantsoa (!ocean)",
 "Mahajanga",
 "Toliara",
 "Antsiranana",
 "Antanifotsy",
 "Ambovombe",
 "Amparafaravola",
 "Taolagnaro",
 "Ambatondrazaka",
 "Mananara Avaratra",
 "Soavinandriana",
 "Mahanoro",
 "Soanierana Ivongo",
 "Faratsiho",
 "Nosy Varika",
 "Vavatenina",
 "Morondava",
 "Amboasary",
 "Manakara",
 "Antalaha",
 "Ikongo",
 "Manjakandriana",
 "Sambava",
 "Fandriana",
 "Marovoay",
 "Betioky",
 "Ambanja",
 "Ambositra",
 "Antsohimbondrona",
 "Mananjary",
 "Tolanaro",
 "Andoany"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
