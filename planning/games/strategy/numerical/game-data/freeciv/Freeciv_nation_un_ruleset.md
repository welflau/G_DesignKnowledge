# Freeciv(nation) · un

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/un.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的un定义

## 正文
```ruleset
[nation_un]

name=_("UN")
plural=_("?plural:UN")
groups="Imaginary"
legend=_("The United Nations believe in human rights and the protection of\
 the weak.")

leaders = {
 "name",                        "sex"
 "Trygve Lie",                  "Male"
 "Dag Hammarskjöld",            "Male"
 "U Thant",                     "Male"
 "Kurt Waldheim",               "Male"
 "Javier Pérez de Cuéllar",     "Male"
 "Boutros Boutros-Ghali",       "Male"
 "Kofi Annan",                  "Male"
 "Ban Ki-moon",                 "Male"
}

ruler_titles = {
 "government",      "male_title",       "female_title"
 "Democracy",       _("Councillor %s"), _("?female:Councillor %s")
 "Communism", _("Secretary-General %s"), _("?female:Secretary-General %s")
}

flag="united_nations"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

cities=
 "Security Council",
 "General Assembly",
 "ECOSOC",
 "Trusteeship Council",
 "ICJ",
 "UNHCR",
 "UNESCO",
 "UNICEF",
 "WHO",
 "WWF",
 "IMF",
 "WTO",
 "UNCTAD",
 "UNDCP",
 "UNDP",
 "UNEP",
 "UNFPA",
 "UNHSP",
 "WFP",
 "UNRWA",
 "INSTRAW",
 "UNICRI",
 "UNITAR",
 "UNRISD",
 "UNIDIR",
 "OHCHR",
 "UNOPS",
 "UNU",
 "UNOOSA",
 "UNSSC",
 "UNAIDS",
 "UNRRA",
 "ILO",
 "FAO",
 "ICAO",
 "IMO",
 "ITU",
 "UPU",
 "WMO",
 "WIPO",
 "IFAD",
 "UNIDO",
 "IRO",
 "INCB",
 "IAEA",
 "ICC"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
