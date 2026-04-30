# Freeciv(nation) · burkinabe

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/burkinabe.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的burkinabe定义

## 正文
```ruleset
[nation_burkinabe]

name=_("Burkinabé")
; pre-2.6 had plain ASCII names
rule_name="Burkinabe"
plural=_("?plural:Burkinabés")
groups="Modern", "African"
legend=_("Formerly Upper Volta, Burkina Faso is a country in inland\
 West Africa. It achieved its independence from France in 1960.")

leaders = {
 "name",                "sex"
 "Maurice Yaméogo",     "Male"
 "Sangoulé Lamizana",   "Male"
 "Saye Zerbo",          "Male"
 "Thomas Sankara",      "Male"
 "Blaise Compaoré",     "Male"
}

flag="burkina_faso"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="fulani", "kanem-bornu", "ivoirian"

cities =
 "Ouagadougou",
 "Bobo-Dioulasso",
 "Koudougou",
 "Banfora",
 "Ouahigouya",
 "Pouytenga",
 "Kaya",
 "Tenkodogo",
 "Fada N'Gourma",
 "Dédougou",
 "Garango",
 "Houndé",
 "Djibo",
 "Koupéla",
 "Réo",
 "Léo",
 "Kongoussi",
 "Gaoua",
 "Gourcy",
 "Pô",
 "Kombissiri",
 "Yako",
 "Niangoloko",
 "Dori",
 "Orodara",
 "Zorgho",
 "Manga",
 "Titao",
 "Nouna",
 "Tougan",
 "Diébougou",
 "Ziniaré",
 "Boulsa",
 "Dano",
 "Bittou",
 "Boromo",
 "Boussé",
 "Solenzo",
 "Toma",
 "Bogandé",
 "Sapouy",
 "Batié",
 "Ouargaye"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
