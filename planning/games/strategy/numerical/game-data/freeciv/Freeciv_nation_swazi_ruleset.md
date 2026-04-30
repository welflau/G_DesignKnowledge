# Freeciv(nation) · swazi

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/swazi.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的swazi定义

## 正文
```ruleset
[nation_swazi]

name=_("Swazi")
plural=_("?plural:Swazis")
groups="Modern", "African"
legend=_("The Swazi are a Bantu people of southern Africa. Under the\
 leadership of Mswati II (1820 - 1868), the Swazis expanded their territory\
 and stabilized the southern frontier with the Zulus.")

leaders = {
 "name",        "sex"
 "Dlamini I",   "Male"
 "Sobhuza I",   "Male"
 "Mswati II",   "Male"
 "Labotsibeni", "Female"
 "Sobhuza II",  "Male"
 "Ntombi",      "Female"
}

ruler_titles = {
 "government",     "male_title",            "female_title"
 "Republic",       _("Spokesman %s"),       _("Spokeswoman %s")
 "Democracy",      _("Principal Chief %s"), _("?female:Principal Chief %s")
}

flag="swaziland"
flag_alt = "rwanda"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="zulu", "xhosa"

; The two capitals at top and the rest in order of population as of 2005
; http://de.wikipedia.org/wiki/Liste_der_Städte_in_Swasiland
cities =
 "Lobamba",
 "Mbabane",
 "Manzini",
 "Big Bend",
 "Malkerns",
 "Nhlangano",
 "Mhlume",
 "Hluti",
 "Simunye",
 "Siteki",
 "Pigg's Peak",
 "Ngomane",
 "Vuvulane",
 "Mpaka",
 "Kwaluseni",
 "Bhunya",
 "Mhlambanyatsi",
 "Mondi",
 "Tabankulu",
 "Hlatikulu",
 "Bulembu",
 "Kubuta",
 "Tjaneni",
 "Sidvokodvo",
 "Lavumisa",
 "Ngwenya",
 "Nsoko",
 "Mankayane"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
