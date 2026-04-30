# Freeciv(nation) · mazovian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/mazovian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的mazovian定义

## 正文
```ruleset
[nation_mazovian]

name=_("Mazovian")
plural=_("?plural:Mazovians")
groups="European", "Medieval"
legend=_("Mazovia is a historic and geographic region of central-eastern Poland.")

leaders = {
 "name",                        "sex"
 "Miecław",                     "Male"
 "Bolesław IV Kędzierzawy",     "Male"
 "Kazimierz II Sprawiedliwy",   "Male"
 "Leszek I Biały",              "Male"
 "Konrad I Mazowiecki",         "Male"
 "Helena Znojemska",            "Female"
 "Janusz II",                   "Male"
 "Janusz III",                  "Male"
 "Konrad III Rudy",             "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Despotism",       _("Prince %s"),          _("Princess %s")
 "Fundamentalism",  _("Archbishop %s"),      _("Mother Superior %s")
 "Monarchy",        _("Grand Prince %s"),    _("Grand Princess %s")
 "Communism",       _("First Secretary %s"), _("?female:First Secretary %s")
}

flag = "mazovia"
flag_alt = "-"
style = "European"
init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "polish", "cuyavian"

cities =
  "Czersk",
"Płock",
"Warszawa",
"Łomża",
"Rawa",
"Dobrzyń",
"Sierpc",
"Mława",
"Żarnów",
"Radom",
"Zakroczym",
"Sochaczew",
"Gostynin",
"Wizna",
"Liw",
"Płońsk",
"Kuczbork",
"Niedzbórz",
"Szreńsk",
"Nur",
"Wyszogród",
"Grójec",
"Ciechanów",
"Przasnysz",
"Ostrołęka",
"Zambrów",
"Drohiczyn",
"Żuromin",
"Pułtusk",
"Kozienice",
"Żyrardów",
"Pruszków",
"Otwock",
"Siedlce",
"Garwolin",
"Zwoleń",
"Skierniewice",
"Łowicz",
"Wyszków",
"Radzymin",
"Warka",
"Iłża",
"Różan",
"Serock"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
