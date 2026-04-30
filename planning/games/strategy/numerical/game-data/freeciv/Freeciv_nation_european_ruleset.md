# Freeciv(nation) · european

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/european.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的european定义

## 正文
```ruleset
[nation_europe]

name=_("European")
plural=_("?plural:Europeans")
groups="Imaginary"
legend=_("The foundation for the European Union was laid in 1957 with the\
 Treaty of Rome. The EU project has developed since then and is beginning to\
 resemble a fledgeling super state. But the question remains: Does such a\
 thing as a common European identity and nation actually exist?")

; Presidents of the European Commission that held office over one year.
leaders = {
 "name",                        "sex"
 "Walter Hallstein",            "Male"
 "Jean Rey",                    "Male"
 "Franco Maria Malfatti",       "Male"
 "Sicco L. Mansholt",           "Male"
 "Roy Jenkins",                 "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Fundamentalism",  _("Pope %s"),         _("Popess %s")
 "Democracy",       _("Commissioner %s"), _("?female:Commissioner %s")
}

flag="europe"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""


conflicts_with="austrian", "belgian", "bulgarian", "czech", "cypriot",
               "danish", "estonian", "finnish", "french", "german",
               "hellenic", "hungarian", "irish", "italian", "latvian",
               "lithuanian", "luxembourgish", "maltese", "dutch", "polish",
               "portuguese", "romanian", "slovakian", "slovenian",
               "spanish", "swedish", "british"
civilwar_nations="austrian", "belgian", "bulgarian", "czech", "cypriot",
               "danish", "estonian", "finnish", "french", "german",
               "hellenic", "hungarian", "irish", "italian", "latvian",
               "lithuanian", "luxembourgish", "maltese", "dutch", "polish",
               "portuguese", "romanian", "slovakian", "slovenian",
               "spanish", "swedish", "british"
cities=
; Sites of EU institutions
 "Brussel / Bruxelles",
 "Lëtzebuerg",
 "Strasbourg",
 "Frankfurt am Main",
 "Den Haag"
; Subsequent cities fetched from city lists of member nations

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
