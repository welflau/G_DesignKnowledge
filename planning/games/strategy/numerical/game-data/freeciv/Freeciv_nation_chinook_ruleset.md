# Freeciv(nation) · chinook

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/chinook.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的chinook定义

## 正文
```ruleset
[nation_chinook]

name=_("Chinook")
plural=_("?plural:Chinooks")
groups="American", "Early Modern"
legend=_("The Chinook Confederacy was a group of communities with common\
 customs and language. They were a sedentary people living along the\
 Columbia river in present-day Oregon and Washington in the United\
 States. Chinook regional influence can be seen in the fact that\
 their tongue became the base of a pidgin language for trade and\
 communication between Native Americans and Whites throughout Oregon,\
 Washington, British Columbia and all the way to Alaska.")

leaders = {
 "name",                "sex"
 "Catherine Troeh",     "Female"
 "Tumulth",             "Male"
 "Comcomly",            "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Monarchy",        _("Great Chief %s"),     _("?female:Great Chief %s")
 "Democracy",       _("Principal Chief %s"), _("?female:Principal Chief %s")
}

flag="clatsop"
flag_alt="-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Nimiipuu", "Salishan"

cities =
 "Multnomah",
 "Wasco",
 "Clatsop",
 "Clackamas",
 "Watlala",
 "Cathlahmahs",
 "Chilluckittequaw",
 "Chahcowah",
 "Wappato",
 "Cathlamet",
 "Wishram",
 "Killaniuck",
 "Skillot",
 "Wackiacum",
 "Wascopa",
 "Clowwewalla",
 "Cushook",
 "Echelut",
 "Kiksht",
 "Willapa",
 "Ilwaco"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
