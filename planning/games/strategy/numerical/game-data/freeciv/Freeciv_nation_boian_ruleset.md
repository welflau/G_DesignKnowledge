# Freeciv(nation) · boian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/boian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的boian定义

## 正文
```ruleset
[nation_boian]

name=_("Boian")
plural=_("?plural:Boii")
groups="Ancient", "European"
legend=_("The Boii were an ancient Celtic tribe or tribal confederation\
 inhabiting Central Europe and Northern Italy. The names of both Bohemia\
 and Bavaria probably derive from this people.")
leaders = {
 "name",                "sex"
 "Magalos",             "Male"
 "Biatec",              "Male"
 "Atis",                "Male"
 "Galatos",             "Male"
}
flag="boii"
flag_alt = "czech"
style = "Celtic"

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Fundamentalism",       _("High Druid %s"),       _("?female:High Druid %s")
}

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Czech", "Bavarian", "Austrian", "Hungarian", "Slovakian",
 "Slovenian", "Friulian", "Milanese", "Tyrolian", "Moravian", "Silesian"
civilwar_nations = "Gallic", "Helvetian", "Illyrian"

cities =
 "Boiodurum",
 "Vindobona",
 "Aquincum",
 "Bononia",
 "Carnuntum",
 "Noreia",
 "Telamon",
 "Gorgobina",
 ; Oppida with unknown original Celtic names:
 "Hallstatt",
 "Manching",
 "Placentia",
 "Sandberg",
 "Bratislava",
 "Zavist",
 "Stradonice",
 "Nevězice",
 "Hrazany",
 "Třísov",
 "Staré Hradisko",
 "Hradiště"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
