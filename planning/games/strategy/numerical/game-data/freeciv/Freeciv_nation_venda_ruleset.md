# Freeciv(nation) · venda

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/venda.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的venda定义

## 正文
```ruleset
[nation_venda]

name = _("Venda")
plural = _("?plural:Vhavenda")
groups="African", "Early Modern", "Medieval"
legend=_("The Vhavenda are a Bantu people in South Africa and Zimbabwe.\
 Once the rulers of the Mapungubwe Kingdom, they now count about one\
 million members, mostly in the province of Limpopo. During the Apartheid\
 Era there existed a Bantustan of Venda.")

leaders = {
 "name",                     "sex"
 "Shiriyadenga",             "Male"
 "Thohoyandou",              "Male"
 "Makhado",                  "Male"
 "Patrick Mphephu",          "Male"
 "Gabriel Ramushwana",       "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Monarchy",        _("Paramount Chief %s"), _("?female:Paramount Chief %s")

}

flag = "venda"
flag_alt = "-"
style = "babylonian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="sotho", "zulu", "swazi"

cities =
 "Mapungubwe",
 "Dzata",
 "Thulamela",
 "Sibasa",
 "Thohoyandou",
 "Mutale",
 "Musina",
 "Malamulele",
 "Dzanani",
 "Mbilwi",
 "Tswime",
 "Tshiendeulu",
 "Tshakhuma",
 "Tshamanyatsha",
 "Musina",
 "Tshivuhla",
 "Lishivha",
 "Matshete",
 "Mulambwane",
 "Madzhie",
 "Fundudzi",
 "Makwarela",
 "Shayandima",
 "Giyani",
 "Tshilamba",
 "Vhutalu",
 "Elim",
 "Phalaborwa",
 "Ngovhela",
 "Vondwe",
 "Phiphidi",
 "Muledane",
 "Shayandima",
 "Manlini"



```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
