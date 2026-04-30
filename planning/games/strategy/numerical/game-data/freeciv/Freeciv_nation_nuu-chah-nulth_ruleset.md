# Freeciv(nation) · nuu-chah-nulth

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/nuu-chah-nulth.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的nuu-chah-nulth定义

## 正文
```ruleset
[nation_nuu-chah-nulth]

name=_("Nuu-chah-nulth")
plural=_("?plural:Nuu-chah-nulth")
groups="American"

legend=_("The Nuu-chah-nulth are a Pacific Northwest people, one of the few\
 Native American peoples to travel in the open ocean and hunt whales. They\
 inhabited most of what is now western Vancouver Island and now number over\
 8,000 individuals. Like other people of the Pacific Northwest, they built\
 large wooden canoes and houses and lived in clan systems.")

leaders = {
 "name",        "sex"
 "Keitlah",     "Male"
 "Tatoosh",     "Male"
 "Nookemis",    "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Democracy",       _("Principal Chief %s"), _("?female:Principal Chief %s")
 "Fundamentalism",  _("Shaman %s"),          _("?female:Shaman %s")
 "Monarchy",        _("Great Chief %s"),     _("?female:Great Chief %s")
}

flag         = "nuu-chah-nulth"
flag_alt     = "-"
style        = "Celtic"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="salishan", "sioux", "chinook"

cities =
 "Ahousaht",
 "Ucluelet",
 "Ehattesaht",
 "Checkleset",
 "Hesquiaht",
 "Kyuquot",
 "Mowachaht",
 "Muchalaht",
 "Nuchatlaht",
 "Huu-ay-aht",
 "Tseshaht",
 "Tla-o-qui-aht",
 "Toquaht",
 "Uchucklesaht",
 "Ditidaht",
 "Pacheedaht",
 "Hupacasath",
 "Hisaawista",
 "Yuquot",
 "Nootk-sitl",
 "Maaqtusiis",
 "Kakawis",
 "Kitsuksis",
 "Opitsaht",
 "Pacheena",
 "Tsu-ma-uss",
 "Tsahaheh",
 "Hitac`u",
 "T’iipis",
 "Tsaxana",
 "Cheewat",
 "Tl'aadiiwa",
 "Tsuxwkwaada",
 "Tsakkawis",
 "Waayaa"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
