# Freeciv(nation) · ligurian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/ligurian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的ligurian定义

## 正文
```ruleset
[nation_ligurian]

name=_("Ligurian")
plural=_("?plural:Ligurians")
groups="Ancient", "European"
legend=_("The Ligures were a pre-Roman tribal complex in what is now\
 Northwestern Italy and Southern France. Their language is of uncertain\
 origin, perhaps Para-Celtic or Pre-Indo-European.")
leaders = {
 "name",                "sex"
 "Budincus",            "Male"
 "Tutomotulus",         "Male"
 "Donnus",              "Male"
 "Cottius",             "Male"
}
flag="ligurian"
flag_alt = "-"
style = "Celtic"

ruler_titles = {
 "government",      "male_title",              "female_title"
 "Monarchy",        _("Paramount Ruler %s"),   _("?female:Paramount Ruler %s")
 "Republic",        _("Consul %s"),            _("?female:Consul %s")
 "Democracy",       _("Spokesman %s"),         _("Spokeswoman %s")
               }

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Genoese", "Piedmontese", "Monegasque", "Western Roman"
civilwar_nations = "Etruscan", "Roman", "Gallic"

cities =
 "Genua",
 "Dertana",
 "Hasta",
 "Eodetia",
 "Vada Sabatia",
 "Albingaunum",
 "Portus Maurici",
 "Monoecus",
 "Nicaea",
 "Savo",
 "Celia",
 "Calanicum",
 "Tibarna",
 "Camillamanus",
 "Retovium",
 "Forum Fulvii",
 "Crixia",
 "Pedo",
 "Forum Germanorum",
 "Carrea Potentia",
 "Monilia",
 "Portus Veneris",
 "Lunae Portus",
 "Segesta",
 "Portus Dolphinus",
 "Paraberae",
 "Bobium Castrum",
 "Industria",
 "Caenia",
 "Tria",
 "Alba Pompeia",
 "Clasudium",
 "Excingomago",
 "Segusio",
 "Cemenelum",
 "Ebrodunum"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
