# Freeciv(nation) · georgian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/georgian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的georgian定义

## 正文
```ruleset
[nation_georgian]

name=_("Georgian")
plural=_("?plural:Georgians")
groups="Ancient", "Medieval", "Early Modern", "Modern", "European", "Asian"
legend=_("The Georgians were one of the first peoples in history to adopt\
 Christianity, in the 300s CE.")

leaders = {
 "name",                        "sex"
 "Kartlos",                     "Male"
 "Giorgi III",                  "Male"
 "Vakhtang I Gorgasali",        "Male"
 "Tamar",                       "Female"
 "Davit IV",                    "Male"
 "Alexandre Bagrationi",        "Male"
 "Merab Kostava",               "Male"
 "Eduard Shevardnadze",         "Male"
}
ruler_titles = {
 "government",     "male_title",        "female_title"
 "Fundamentalism", _("Patriarch %s"),   _("Matriarch %s")
}
flag="georgia"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "abkhaz", "ossetian"

cities =
 "Tbilisi (river)",
 "Kutaisi",
 "Batumi",
 "Rustavi (river)",
 "Gori (river)",
 "Tskhinvali",
 "Akhalkalaki",
 "Zugdidi",
 "Sokhumi (ocean)",
 "Poti (ocean)",
 "Supsa",
 "Akhaltsikhe",
 "Chiatura",
 "Gagra",
 "Lagodekhi",
 "Mtskheta",
 "Rustavi",
 "Telavi",
 "Akhmeta",
 "Ambrolauri",
 "Bolnisi",
 "Dusheti",
 "Gudauta",
 "Jvari",
 "Kobuleti",
 "Kazreti",
 "Khashuri",
 "Marneuli",
 "Ninotsminda",
 "Ochamchire",
 "Pasanauri",
 "Samtredia",
 "Senaki",
 "Tianeti",
 "Tq'varcheli",
 "Tsalka",
 "Tsiteli-Tsq'aro",
 "Tsnori",
 "Vale"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
