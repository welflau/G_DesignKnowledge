# Freeciv(nation) · parthian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/parthian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的parthian定义

## 正文
```ruleset
[nation_parthian]

name=_("Parthian")
plural=_("?plural:Parthians")
groups="Ancient", "Asian"
legend=_("The Parthians were originally a nomadic people from Central Asia\
 who inhabited the Parthia region of the Seleucid Empire. Under the\
 leadership of the satrap Arsakes they drove the Seleucids from Iran, where\
 they created their own strong empire. Their culture was Hellenistic.")
leaders = {
 "name",                "sex"
 "Andragoras",          "Male"
 "Arsakes I",           "Male"
 "Arsakes II",          "Male"
 "Phriapatios",         "Male"
 "Phraates I",          "Male"
 "Artabanos I",         "Male"
 "Gotarzes I",          "Male"
 "Sanatrukes",          "Male"
 "Vonones I",           "Male"
 "Vologases I",         "Male"
 "Vologases II",        "Male"
 "Vologases III",       "Male"
 "Osroes I",            "Male"
 "Artabanos IV",        "Male"
}
flag="parthia"
flag_alt = "iran"
style = "Classical"

ruler_titles = {
 "government",    "male_title",      "female_title"
 "Anarchy",       _("Usurper %s"),   _("?female:Usurper %s")
 "Despotism",     _("Satrap %s"),    _("?female:Satrap %s")
 "Monarchy",      _("Shah %s"),      _("Shahbanu %s")
}

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Iranian", "Persian", "Iraqi", "Kurdish", "Turkmen",
 "Seljuk", "Ghaznavid", "Babylonian", "Assyrian" ; Median
civilwar_nations = "Saka", "Persian", "Kurdish", "Seleucid", "Armenian"

cities =
 "Ktesiphon",
 "Agbatana",
 "Babylon",
 "Hatra",
 "Dara",
 "Akra",
 "Babak",
 "Karrhai",
 "Nisa",
 "Behistun",          ;archaeological site
 "Dura-Europas",
 "Zenodotium",
 "Vologasia",
 "Urfa",
 "Tambrax",
 "Traxiane",
 "Praaspa",
 "Nihavand",
 "Zapaortenon",
 "Spasini",
 "Tagai",
 "Nisibis",
 "Taxila",
 "Zabdikene",
 "Tapuria",
 "Seleukia",
 "Solake",
 "Oratha",
 "Nikephorion",
 "Nisaia",
 "Margiane",
 "Mesene",            ;Charax
 "Kangavar",
 "Gordyene",
 "Edessa"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
