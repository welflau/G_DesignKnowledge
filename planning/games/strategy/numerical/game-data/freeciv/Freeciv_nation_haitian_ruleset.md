# Freeciv(nation) · haitian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/haitian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的haitian定义

## 正文
```ruleset
[nation_haitian]

name=_("Haitian")
plural=_("?plural:Haitians")
groups="Modern", "American"
legend=_("A slave rebellion led Haiti to independence in 1804. It was the\
 first independent black republic and the second independent country in\
 the Americas.")

leaders = {
 "name",                        "sex"
 "Tousen Louvèti",              "Male"
 "Jan Jak Desalin",             "Male"
 "Anri Kristòf ",               "Male"
 "Jan Pyè Bwaye",               "Male"
 "Aleksann Petyon ",            "Male"
 "Pyè Nò Aleksi",               "Male"
 "Fosten Soulouk",              "Male"
 "'Papa Dok' Divalye",          "Male"
 "Simone Ovide Divalye",        "Female"
 "Jan Bètran Aristid",          "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism", _("President-for-Life %s"), _("?female:President-for-Life %s")
 "Monarchy",        _("Emperor %s"),      _("Empress %s")
}

flag="haiti"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations =  "dominicano", "taino"

cities =
 "Pòtoprens (ocean)",
 "Kap Ayisyen (ocean)",
 "Gonayiv",
 "Kafou",
 "Dèlma",
 "Petyonvil",
 "Sen Mak",
 "Okay",
 "Vèrèt",
 "Pòdpè (ocean)",
 "Jakmèl",
 "Lenbe",
 "Jeremi",
 "Ti Rivyè Latibonit (river)",
 "Ench",
 "Tigwav",
 "Dedin",
 "Desalin",
 "Sen Lwi dinò",
 "Sen Michèl Latalay",
 "Leyogàn",
 "Fòlibète",
 "Twou dinò",
 "Wanament",
 "Mibalè",
 "Grann Rivyè dinò (river)",
 "Laskawobas",
 "Ansdeno",
 "Gwo Mòn",
 "Ansagalè",
 "Piyon",
 "Kwadèbouke",
 "Dam Mari",
 "Miragwàn",
 "Sen Rafayèl",
 "Aken",
 "Kenskòf",
 "Fondènèg",
 "Monben Kwochi",
 "Kòniyon",
 "Lèzanglè",
 "Mayisad",
 "Tomasik",
 "Grangwav",
 "Milo",
 "Jan Rabèl",
 "Dondon",
 "Lakayè",
 "Kabarè",
 "Ans Wouj",
 "Tomazo",
 "Wozo",
 "Tomonn",
 "Obòy",
 "Pilat",
 "Gresye",
 "Plezans"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
