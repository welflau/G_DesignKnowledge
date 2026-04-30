# Freeciv(nation) · mitanni

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/mitanni.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的mitanni定义

## 正文
```ruleset
[nation_mitanni]

name=_("Mitanni")
plural=_("?plural:Mitanni")
groups="Ancient", "Asian"
legend=_("Mitanni was an ancient Hurrian kingdom in what is now Northern\
 Syria and Iraq. Mitanni was at the height of its power during the 14th\
 century BCE, during which it rivalled Egypt.")
leaders = {
 "name",              "sex"
 "Artašumara",        "Male"
 "Artatama I",        "Male"
 "Artatama II",       "Male"
 "Kirta",             "Male"
 "Paršatatar",        "Male"
 "Šattiwaza",         "Male"
 "Šattuara",          "Male"
 "Šauštatar",         "Male"
 "Šuttarna I",        "Male"
 "Šuttarna II",       "Male"
 "Šuttarna III",      "Male"
 "Tušratta",          "Male"
 "Wasašatta",         "Male"
}
flag="mitanni"
flag_alt = "-"
style = "Babylonian"

ruler_titles = { "government",    "male_title",      "female_title"
                 "Anarchy",       _("Usurper %s"),   _("?female:Usurper %s")
                 "Despotism",     _("Prince %s"),    _("Princess %s")
               }

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "syrian", "iraqi", "israeli", "kurdish", "seleucid"
civilwar_nations = "hittite", "aramean", "assyrian", "israelite", "phoenician"

cities =
"Waššukanni",
"Kargamiš",
"Halap",
"Emar",
"Tunip",
"Qatna",
"Kadeš",
"Urkiš",
"Harran",
"Alalakh",
"Ugarit",
"Terqa",
"Nagar",
"Arrapha",
"Nuzi",
"Adanya",
"Kummani",
"Kurruhanni",
"Qattara",
"Ninive",
"Assur",
"Tell Fekheriye",
"Tell Sheikh Hamad",
"Tell Ahmar",
"Tell Chuera"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
