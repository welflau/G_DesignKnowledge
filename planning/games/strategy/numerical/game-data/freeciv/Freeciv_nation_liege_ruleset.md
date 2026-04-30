# Freeciv(nation) · liege

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/liege.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的liege定义

## 正文
```ruleset
[nation_liege]

name   = _("Liège")
; pre-2.6 had plain ASCII names
rule_name="Liege"
plural = _("?plural:Liègeans")
groups = "Medieval", "Early Modern", "European"
legend = _("Liège was constituted in ecclesiastic principalty in 985,\
 when Bishop Notger was granted the control of several cities in current Belgium.\
 As a federated state of the Holy Roman Empire, it was characterized\
 with large civil liberties for which liègean struggled strongly for.\
 It lasted until 1792, when the recently formed Republic of Liège voted\
 the union with revolutionary France.\
 Liège played later a major role in the Belgian independance.")

leaders = {
 "name",                   "sex"
 "Notger",                 "Male"
 "Wazon",                  "Male"
 "Albert de Cuyck",        "Male"
 "Érard de la Marck",      "Male"
 "Jean-Nicolas Bassenge",  "Male"
 "Joseph Bologne",         "Male"
 "Julienne de Cornillon",  "Female"
 "Théroigne de Méricourt", "Female"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Monarchy",        _("Prince %s"),         _("?female:Princess %s")
 "Democracy",       _("Prime Minister %s"), _("?female:Prime Ministress %s")
 "Fundamentalism",  _("Prince-Bishop %s"),  _("Mother Superior %s")
 "Republic",        _("Regent %s"),         _("Regent %s")
}

flag     = "luik"
flag_alt = "belgium"
style    = "Celtic"

init_techs = ""
init_buildings = ""
init_units = ""
conflicts_with = "belgian", "walloon", "flemish"
civilwar_nations = "belgian", "walloon", "flemish"

cities =
 "Liège",
 "Tongeren",
 "Huy",
 "Dinant",
 "Maastricht",
 "Bouillon",
 "Ciney",
 "Thuin",
 "Fosses-la-Ville",
 "Couvin",
 "Châtelet",
 "Sint-Truiden",
 "Visé",
 "Waremme",
 "Borgloon",
 "Hasselt",
 "Maaseik",
 "Bilzen",
 "Beringen",
 "Herk-de-Stad",
 "Bree",
 "Stokkem",
 "Hamont",
 "Peer",
 "Verviers",
 "Seraing",
 "Herstal",
 "Ans",
 "Chaudfontaine",
 "Fexhe",
 "Awans",
 "Waroux",
 "Amay"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
