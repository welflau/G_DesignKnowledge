# Freeciv(nation) · fijian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/fijian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的fijian定义

## 正文
```ruleset
[nation_fijian]

name=_("Fijian")
plural=_("?plural:Fijians")
groups="Oceanian", "Modern"
legend=_("Fiji is the most populous of the small Oceanian island states.\
 It consists of Viti Levu, Vanua Levu and hundreds of smaller islands.\
 Settled by Polynesians, it became a British colony in the 19th century.\
 Fiji has been independent from Britain since 1970. Since then the\
 country's politics have been characterized by ethnic tensions between\
 Indo-Fijians and indigenous Fijians.")

leaders = {
 "name",                        "sex"
 "Seru Epenisa Cakobau",        "Male"
 "Kamisese Mara",               "Male"
 "S. M. Koya",                  "Male"
 "Penaia Ganilau",              "Male"
 "Sitiveni Rabuka",             "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Monarchy",        _("Paramount Chief %s"), _("?female:Paramount Chief %s")
}

flag="fiji"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""

init_units=""
civilwar_nations = "polynesian", "indian"

cities =
 "Suva",
 "Nasinu",
 "Nausori",
 "Lautoka",
 "Nadi",
 "Labasa",
 "Lami",
 "Ba",
 "Sigatoka",
 "Savusavu",
 "Vatukoula",
 "Navua",
 "Rakiraki",
 "Levuka",
 "Tavua",
 "Deuba",
 "Pacific Harbour",
 "Seaqaqa",
 "Navouvalu",
 "Korvou",
 "Bau",
 "Koro-ni-O",
 "Lomaloma",
 "Lovoni",
 "Namatakula",
 "Navala",
 "Somosomo",
 "Viseisei",
 "Vunavikaloa",
 "Yalalevu",
 "Ahau"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
