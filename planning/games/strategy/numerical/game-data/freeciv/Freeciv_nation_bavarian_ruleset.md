# Freeciv(nation) · bavarian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/bavarian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的bavarian定义

## 正文
```ruleset
[nation_bavarian]

name=_("Bavarian")
plural=_("?plural:Bavarians")
groups="Medieval", "Early Modern", "European"
legend=_("Bavaria, before national unification in 1870 CE, was one of the\
 largest of the German kingdoms.") 

leaders = {
 "name",                "sex"
 "Tassilo III",         "Male"
 "Welf I",              "Male"
 "Maximilian",          "Male"
 "Adelheid",            "Female"
 "Max II Emanuel",      "Male"
 "Maximilian I Joseph", "Male"
 "Ludwig II",           "Male"
 "Kurt Eisner",         "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("Duke %s"),         _("Duchess %s")
 "Fundamentalism",  _("Bishop %s"),       _("Mother Superior %s")
 "Democracy",       _("Minister-President %s"), _("?female:Minister-President %s")
}

flag="bavarian"
flag_alt = "-"
style = "European"
init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "franconian", "austrian", "tyrolian", "palatinate"

cities =
 "München",
 "Regensburg",
 "Ingolstadt",
 "Landshut",
 "Rosenheim",
 "Eichstätt",
 "Passau",
 "Straubing",
 "Mühldorf",
 "Freising",
 "Deggendorf",
 "Erding",
 "Freilassing",
 "Altötting",
 "Pfaffenhofen",
 "Vilshofen",
 "Plattling",
 "Traunstein",
 "Burghausen",
 "Dingolfing",
 "Nürnberg",
 "Augsburg",
 "Würzburg",
 "Fürth",
 "Erlangen",
 "Bayreuth",
 "Bamberg",
 "Aschaffenburg",
 "Kempten",
 "Neu-Ulm",
 "Schweinfurt",
 "Hof",
 "Amberg",
 "Dachau",
 "Ansbach",
 "Neumarkt",
 "Garmisch-Partenkirchen",
 "Bad Kissingen",
 "Rothenburg ob der Tauber",
 "Donauwörth",
 "Bad Reichenhall",
 "Marktredwitz",
 "Füssen",
 "Berchtesgaden",
 "Landau an der Isar",
 "Neustadt an der Aisch"




```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
