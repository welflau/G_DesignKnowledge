# Freeciv(nation) · inuit

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/inuit.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的inuit定义

## 正文
```ruleset
[nation_inuit]

name=_("Inuit")
plural=_("?plural:Inuits")
groups="American"
legend=_("The Inuits are a group of peoples inhabiting the Arctic areas\
 of North America and Siberia. The Canadian territory of Nunavut has a\
 majority population of Inuits; the name of the territory means \"our\
 land\" in Inuktitut.")

leaders = {
 "name",                "sex"
 "Abe Okpik",           "Male"
 "Helen Maksagak",      "Female"
 "Paul Okalik",         "Male"
 "Eva Aariak",          "Female"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Fundamentalism",  _("Shaman %s"),        _("?female:Shaman %s")
 "Monarchy",        _("Great Chief %s"),     _("?female:Great Chief %s")
 "Republic",        _("Spokesman %s"),       _("Spokeswoman %s")
 "Democracy",       _("Principal Chief %s"), _("?female:Principal Chief %s")
}

flag="nunavut"
flag_alt = "greenland" ; used previously
style = "European"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="Canadian", "Aleut", "Greenlander"

cities =
; Communities recognised by the Government of Nunavut
 "Iqaluit",		; Frobisher Bay
 "Kangiqiniq",
 "Arviat",		; Eskimo Point
 "Qamani’tuaq",
 "Iglulik",
 "Iqaluktuuttiaq",
 "Pangniqtuuq",
 "Mittimatalik",
 "Qurluqtuq",
 "Kinngait",
 "Uqsuqtuuq",
 "Kangiqtugaapik",
 "Talurjuaq",
 "Salliit",
 "Naujaat",
 "Sanikiluaq",
 "Ikpiarjuk",
 "Arviligjuaq",
 "Sanirajak",
 "Qikiqtarjuaq",
 "Kimmirut",		; Lake Harbour
 "Tikirarjuaq",
 "Igluligaarjuk",
 "Qausuittuq",
 "Aujuittuq"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
