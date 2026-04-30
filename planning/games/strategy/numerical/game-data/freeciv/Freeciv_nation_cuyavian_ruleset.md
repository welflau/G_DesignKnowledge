# Freeciv(nation) · cuyavian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/cuyavian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的cuyavian定义

## 正文
```ruleset
[nation_cuyavian]

name=_("Cuyavian")
plural=_("?plural:Cuyavians")
groups="European", "Medieval"
legend=_("Cuyavia is a historical region in Northern-Central Poland,\
 bordered to the East by Masovia, on the West by Greater Poland and on the\
 North by Pomerania.")
leaders = {
 "name",                      "sex"
 "Kazimierz I Kujawski",      "Male"
 "Leszek Czarny",             "Male"
 "Kazimierz II Kujawski",     "Male"
 "Władysław Garbaty",         "Male"
 "Kazimierz III Gniewkowski", "Male"
 "Leszek Inowrocławski",      "Male"
 "Władysław Biały",           "Male"	   
}
flag="cuyavia"
flag_alt = "-"
style = "Celtic"

ruler_titles = {
 "government",     "male_title",         "female_title"
 "Despotism",      _("Prince %s"),       _("Princess %s")
 "Monarchy",       _("Grand Prince %s"), _("Grand Princess %s")
 "Fundamentalism", _("Bishop %s"),       _("Mother Superior %s")
}

init_techs=""
init_buildings=""
init_units=""

conflicts_with="polish", "slavic" ; gothic polanian
civilwar_nations = "greater polish", "mazovian", "polish"

cities =
 "Włocławek",
 "Inowrocław",
 "Kruszwica",
 "Gniewkowo",
 "Bydgoszcz",
 "Brześć Kujawski",
 "Radziejów",
 "Raciążek",
 "Solec Kujawski",
 "Strzelno",
 "Pakość",
 "Przedecz",
 "Koronowo",
 "Fordon",
 "Gębice",
 "Skulsk",
 "Podgórz",
 "Sompolno",
 "Chodecz",
 "Izbica Kujawska",
 "Lubień Kujawski",
 "Lubraniec",
 "Służewo",
 "Kowal",
 "Aleksandrów Kujawski",
 "Nowa Wieś Wielka"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
