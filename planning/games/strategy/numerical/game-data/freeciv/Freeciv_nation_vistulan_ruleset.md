# Freeciv(nation) · vistulan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/vistulan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的vistulan定义

## 正文
```ruleset
[nation_vistulan]

name=_("Vistulan")
plural=_("?plural:Vistulans")
groups="European", "Medieval"
legend=_("Vistulans were a West Slavic tribe inhabiting what is today\
 the area of Lesser Poland. Little is known about their history. Many\
 historians agree that throughout the early Middle Ages Vistulans were\
 one of the strongest Slavic tribes of today's Poland, but conflicts\
 with Great Moravia and Magyars prevented them from forming a stable and\
 lasting state. Eventually, the lands of Vistulans and several other\
 Slavic tribes were unified by Polonians, who formed the first Polish\
 state in the 10th century.")

; legendary and alleged rulers, no Vistulan leader is known for sure
leaders = {
 "name",                 "sex"
 "Krak",                 "Male"
 "Wanda",                "Female"
 "Dobromir",             "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("Chieftain %s"),    _("?female:Chieftain %s")
 "Fundamentalism",  _("Druid %s"),        _("?female:Druid %s")
 "Monarchy",        _("Grand Prince %s"), _("Grand Princess %s")
}

flag = "vistulan"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

conflicts_with =
 "polish",
 "milanese"

civilwar_nations = 
 "silesian", 
 "polish"

cities =
 "Kraków (river)",
 "Wiślica (river)",
 "Sandomierz",
 "Stradów",
 "Demblin",
 "Naszacowice",
 "Stawy",
 "Zawada Lanckrońska",
 "Trzcinica nad Ropą (river)",
 "Bocheniec",
 "Karkuszowice",
 "Przemyśl",
 "Skawina",
 "Wieliczka",
 "Myślenice",
 "Krzeszowice",
 "Tarnów",
 "Zakopane (mountains)",
 "Szczawnica",
 "Bukowno",
 "Nowy Targ",
 "Nowy Sącz",
 "Olkusz",
 "Bochnia",
 "Gorlice",
 "Mielec",
 "Dębica",
 "Jasło",
 "Tarnobrzeg"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
