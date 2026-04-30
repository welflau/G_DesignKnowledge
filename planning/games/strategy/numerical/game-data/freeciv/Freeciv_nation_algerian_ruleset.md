# Freeciv(nation) · algerian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/algerian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的algerian定义

## 正文
```ruleset
[nation_algerian]

name=_("Algerian")
plural=_("?plural:Algerians")
groups="Modern", "African"
legend=_("Algeria is an Arabic nation in North Africa. It is historically\
 inhabited by the Berber people.")

leaders = {
 "name",                "sex"
 "Ahmed Ben Bella",     "Male"
 "Houari Boumédienne",  "Female"
 "Kahina",              "Male"
 "Kusayla",             "Male"
 "Abd al-Qadir",        "Male"
 "Mohammad Boudiaff",   "Male"
}

ruler_titles = {
 "government",      "male_title",              "female_title"
 "Communism",       _("Secretary General %s"), _("?female:Secretary General %s")
 "Despotism",       _("%s Dey"),               _("?female:%s Dey")
 "Fundamentalism",  _("Caliph %s"),            _("Calipha %s")
}

flag="algeria"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "Tunisian", "Libyan", "Amazigh"

cities =
 "Algiers",
 "Oran",
 "Biskra",
 "Sidi Bel Abbès",
 "Annaba",
 "Constantine",
 "Tiemcen",
 "Béchar",
 "Tindouf",
 "Ghardaïa",
 "Sétif",
 "Bejaïa",
 "El Golea",
 "I-n-Salah",
 "Ghat",
 "Tamanrasset",
 "Adrar",
 "Ech Cheliff",
 "El Kala",
 "Timimoun",
 "El Oued",
 "Bordj Omar Driss"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
