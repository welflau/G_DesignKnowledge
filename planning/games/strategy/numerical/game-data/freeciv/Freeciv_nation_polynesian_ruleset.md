# Freeciv(nation) · polynesian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/polynesian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的polynesian定义

## 正文
```ruleset
[nation_polynesian]

translation_domain="freeciv"

name=_("Polynesian")
plural=_("?plural:Polynesians")
groups= "Oceanian", "Core"
legend=_("Polynesian culture stretches from Hawaii to New Zealand to\
 Easter Island and covers all the islands in between.")

leaders = {
 "name",                "sex"
 "Solomon Mamaloni",    "Male"
 "Malietoa Tanumafili", "Male"
 "Tofilau Eti Alesana", "Male"
 "Kamehameha",          "Male"
 "Pomare IV",           "Female"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Monarchy",        _("Great Chief %s"),     _("?female:Great Chief %s")
 "Republic",        _("Spokesman %s"),       _("Spokeswoman %s")
 "Democracy",       _("Principal Chief %s"), _("?female:Principal Chief %s")
}

flag="polynesian"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "hawaiian", "fijian", "maori", "rapa nui", "samoan",
 "tahitian", "tongan"
civilwar_nations = "hawaiian", "fijian", "maori", "rapa nui", "samoan",
 "tahitian", "tongan"

cities =
 "Apia",	; Samoa
 "Nuku'alofa",	; Tonga
 "Lautoka",	; Fiji
 "Pape'ete",	; Tahiti, French Polynesia
 "Hanga Roa",	; Easter Island
 "Honolulu",	; Hawaii
 "Hilo",	; Hawaii
 "Lihue",	; Hawaii
 "Hookena",	; Hawaii
 "Fongafale",	; Tuvalu
; Islands
 "Kapingamarangi",
 "Anuta",
 "Emae",
 "Mele",
 "Niue",
 "Nukumanu",
 "Nukuoro",
 "Pileni",
 "Rotuma",
 "Sikaiana",
 "Takuu",
 "Tikopia"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
