# Freeciv(nation) · raramuri

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/raramuri.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的raramuri定义

## 正文
```ruleset
[nation_raramuri]

name=_("Rarámuri")
; pre-2.6 had plain ASCII names
rule_name="Raramuri"
plural=_("?plural:Rarámuris")
groups= "American"
legend=_("The Rarámuri or Tarahumara live in the canyons of the Sierra\
 Madre Occidental in the north of Mexico. They are well known for their\
 endurance; their traditions include running long distances while\
 kicking wooden balls in races that last up to several days. In 1891 a\
 Rarámuri uprising in Tomochi was brutally repressed by the Mexican\
 authorities.")

leaders = {
 "name",                "sex"
 "Candameña",           "Male"
 "Basaseachi",          "Female"
 "Teresa Urrea",        "Female"
 "Cruz Chávez",         "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Fundamentalism",  _("Shaman %s"),    _("?female:Shaman %s")
}

flag="raramuri"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "hopi", "aztec"

cities =
 "Urike",
 "Tomochi",
 "Basasachi",
 "Kusarare",
 "Bokoina",
 "Wachochi",
 "Kusiwiriachi",
 "Serokawi",
 "Batopilas",
 "Mawarichi",
 "Sisowichi",
 "Temosachi",
 "Uruwachi",
 "Yepachi",
 "Areponapuchi",
 "Yepomera",
 "Kokomorachi",
 "Kajurichi",
 "Wevachi",
 "Kawisori",
 "Yokivo",
 "Sojawachi",
 "Panalachi",
 "Karichi",
 "Tajirachi",
 "Okoviachi",
 "Tejolokachi",
 "Temoris",
 "Gasogachi",
 "Jikamorachi",
 "Bawichivo",
 "Matachi",
 "Tejolocachi",
 "Pakime",
 "Yekora",
 "Tonochi",
 "Tekoripa",
 "Bakanora",
 "Tosanachi",
 "Tabaráopa"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
