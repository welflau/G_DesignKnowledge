# Freeciv(nation) · senegalese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/senegalese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的senegalese定义

## 正文
```ruleset
[nation_senegalese]

name=_("Senegalese")
plural=_("?plural:Senegalese")
groups="Modern", "African"
legend=_("Senegal is the westernmost country of mainland Africa. It has\
 been independent from France since 1960. Senegal is relatively stable\
 and democratic compared to its neighbors.")

leaders = {
 "name",                        "sex"
 "Léopold Sédar Senghor",       "Male"
 "Abdou Diouf",                 "Male"
 "Mame Madior Boye",            "Female"
}
ruler_titles = {
 "government",      "male_title",         "female_title"
 "Fundamentalism",  _("Grand Mufti %s"), _("?female:Grand Mufti %s")
 "Monarchy",        _("Mansa %s"),       _("?female:Mansa %s")
}
flag= "senegal"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="jolof"
civilwar_nations="malian", "jolof", "gambian", "fulani"

cities =
 "Dakar (ocean)",
 "Saint-Louis",
 "Touba",
 "Thiès",
 "Pikine",
 "Kaolack",
 "Guediawaye",
 "Mbour",
 "Rufisque",
 "Ziguinchor",
 "Diourbel",
 "Louga",
 "Tambacounda",
 "Mbacké",
 "Kolda",
 "Richard Troll",
 "Bargny",
 "Tivaouane",
 "Joal-Fadiouth",
 "Dahra",
 "Kaffrine",
 "Bignona",
 "Fatick",
 "Vélingara",
 "Bambey",
 "Sébikhotane",
 "Dagana",
 "Sédhiou",
 "Nguékhokh",
 "Kédougou",
 "Pout",
 "Kayar",
 "Matam",
 "Mékhé",
 "Nioro du Rip",
 "Ouro Sogui",
 "Kébémer",
 "Ndioum",
 "Koungheul",
 "Guinguinéo",
 "Linguère",
 "Khombole",
 "Bakel",
 "Sokone",
 "Diamniadio",
 "Mboro",
 "Thiadiaye",
 "Goudomp",
 "Podor",
 "Gossas"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
