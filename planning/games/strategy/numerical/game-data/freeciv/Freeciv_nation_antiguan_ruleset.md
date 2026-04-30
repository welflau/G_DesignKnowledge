# Freeciv(nation) · antiguan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/antiguan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的antiguan定义

## 正文
```ruleset
[nation_antiguan]

name=_("Antiguan and Barbudan")
plural=_("?plural:Antiguans and Barbudans")
groups="Modern", "American"
legend=_("Antigua and Barbuda is a country in the Eastern Caribbean\
 consisting of the two eponymous islands as well as a number of smaller\
 islets. The country has been independent from the United Kingdom since\
 1981.")

leaders = {
 "name",                   "sex"
 "Christopher Codrington", "Male"
 "Prince Klaas Stone",     "Male"
 "Vere Cornwall Bird",     "Male"
 "Baldwin Spencer",        "Male"
 "Louise Lake-Tack",       "Female"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Fundamentalism",  _("Bishop %s"),          _("?female:Bishop %s")
}
flag="antigua_and_barbuda"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Dominican", "kittitian and nevisian"

cities =
 "Saint John's",
 "Codrington",
 "English Harbour (ocean)",
 "Carlisle",
 "Old Road",
 "Parham",
 "Freetown",
 "All Saints",
 "Liberta",
 "Potters Village",
 "Bolands",
 "Swetes",
 "Seaview Farm (ocean)",
 "Pigotts",
 "Clare Hill (hills)",
 "Willikies",
 "Bendals",
 "New Winthropes",
 "Jennings",
 "Cedar Grove",
 "Urlings",
 "Freemans Village",
 "Crosbies",
 "Buckleys",
 "Hodges Bay (ocean)",
 "Pares",
 "Falmoth",
 "Paradise View",
 "Emanuel",
 "Redonda",
 "Bethesda",
 "Ebenezer",
 "Seatons",
 "Five Islands",
 "Newfield",
 "John Hughes",
 "Greencastle",
 "Cobbs Cross",
 "Marble Hill (hills)",
 "Glanvilles",
 "Coolidge",
 "Christian Hill (hills)",
 "Table Hill Garden (hills)",
 "Fitches Creek",
 "Saint Philips",
 "Johnsons Point",
 "Crabb Hill (hills)",
 "Cobbs Cross",
 "Marble Hills",
 "Sawcolts (hills)"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
