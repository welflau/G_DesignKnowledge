# Freeciv(nation) · sabine

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/sabine.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的sabine定义

## 正文
```ruleset
[nation_sabine]

name=_("Sabine")
plural=_("?plural:Sabines")
groups="Ancient", "European"
legend=_("The Sabines were an Italic tribe whose language was closest to\
 Umbrian. They had an impact on the history of Rome. The Sabines and\
 the early Roman Republic regularly warred against each other, but\
 eventually the Sabines were assimilated into the Roman culture. Several\
 Roman families prided themselves on their Sabine origins.")
leaders = {
 "name",                         "sex"
 "Titus Tatius",                 "Male"
 "Numa Pompilius",               "Male"
 "Ancus Marcius",                "Male"
 "Quintus Sertorius",            "Male"
 "Attius Clausus",               "Male"
 "Gaius Sallustius Crispus",     "Male"
 "Marcus Terentius Varro",       "Male"
;The Roman gentes Claudius and Valerius are of Sabine origin
 "Claudia",                      "Female"
 "Valeria",                      "Female"
}
ruler_titles = {
 "government",      "male_title",      "female_title"
 "Anarchy",         _("Usurper %s"),   _("?female:Usurper %s")
 "Democracy",       _("Tribune %s"),   _("?female:Tribune %s")
 "Republic",        _("Consul %s"),    _("?female:Consul %s")
}
flag="sabinium"
flag_alt = "rome"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Western Roman", "Italian", "Papal", "Ostrogothic"
               ; "Langobardic"
civilwar_nations = "Roman", "Samnite"

; The Latin city names come from ancient Sabinium region.

cities =
 "Reate",
 "Nursia",
 "Interocrea",
 "Amiternum",
 "Foruli",
 "Cutilae",
 "Cures",
 "Varia",
 "Trebula Mutusca",
 "Trebula Suffenas",
 "Eretum",
 "Forum Novum",
 "Praeneste",
 "Casperia",
 "Cantalupus in Sabina",
 "Tibur",                        ;Tivoli
 "Treba",
 "Scaptia",
 "Ficulnea",
 "Corniculum",
 "Nussa",
 "Aquae Cutiliae",
 "Trebula Balliensis"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
