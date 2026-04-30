# Freeciv(nation) · ruthenian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/ruthenian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的ruthenian定义

## 正文
```ruleset
[nation_ruthenian]

name=_("Kievan Rus'")
plural=_("?plural:Kievan Rus'")
rule_name="Ruthenian"
groups="European", "Medieval"
legend=_("The Kievan Rus' were a Medieval Slavic monarchy. It was\
 centered in Kiev after that city was conquered by Oleg of Novgorod.\
 In the 13th century the Rus' succumbed to a Mongol invasion. The Rus'\
 were the precursors of the modern East Slavic nations.")

leaders = {
 "name",                        "sex"
 "Oleg",                        "Male"
 "Igor",                        "Male"
 "Olga",                        "Female"
 "Sviatoslav I Veliky",         "Male"
 "Yaropolk I",                  "Male"
 "Volodimer Veliky",            "Male"
 "Sviatopolk Okayanny",         "Male"
 "Yaroslav Mudry",              "Male"
 "Iziaslav I",                  "Male"
 "Volodimer II Monomah",        "Male"
 "Mstislav I",                  "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("Prince %s"),       _("Princess %s")
 "Monarchy",        _("Grand Prince %s"), _("Grand Princess %s")
 "Fundamentalism",  _("Patriarch %s"),    _("Matriarch %s")
}

flag = "kiev"
flag_alt = "russia"
style = "celtic"

init_techs=""
init_buildings=""
init_units=""
conflicts_with = "russian", "ukrainian", "belarusian", "muscovite", "rusyn"
civilwar_nations = "muscovite", "ukrainian", "belarusian", "novgorodian", "rusyn"

cities =
 "Kiev",
 "Novgorod",
 "Volodimer", ;Vladimir
 "Chernigov",
 "Galich",
 "Pereyaslavl",
 "Peresechen",
 "Polotsk",
 "Smolensk",
 "Suzdal",
 "Pskov",
 "Peremyshl",
 "Lyubech",
 "Cherven",
 "Turov",
 "Moskva",
 "Ryazan",
 "Kursk",
 "Belgorod",
 "Nizhny Novgorod",
 "Minsk",
 "Vitebsk",
 "Ladoga",
 "Belo Ozero",
 "Belaya Cerkov",
 "Yaroslavl",
 "Novgorod Seversky",
 "Azov",
 "Tmutarakan",
 "Sarakel",
 "Rostov",
 "Murom",
 "Novgorod-Seversky",
 "Oleshye",
 "Peresechen",
 "Terebovl",
 "Pereyaslavl",
 "Berestye",
 "Toropets"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
