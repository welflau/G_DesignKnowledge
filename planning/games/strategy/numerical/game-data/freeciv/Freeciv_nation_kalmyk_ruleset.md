# Freeciv(nation) · kalmyk

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/kalmyk.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的kalmyk定义

## 正文
```ruleset
[nation_kalmyk]

name=_("Kalmyk")
plural=_("?plural:Kalmyks")
groups="European", "Early Modern"
legend=_("The Kalmyks are a Western Mongolian ethnic group living in\
 Kalmykia in southern Russia. They migrated to the Caspian plains in the\
 17th century and formed a khanate that was allied with Russia. The\
 Kalmyks are the only Buddhist nation of Europe.")

leaders = {
 "name",                "sex"
 "Esen",                "Male"
 "Kho Orluk",           "Male"
 "Ayuka",               "Male"
 "Ubashi",              "Male"
 "Menko Bormanzhinov",  "Male"
 "Oka Gorodovikov",     "Male"
 "Kirsan Ilyumzhinov",  "Male"
}

ruler_titles = {
 "government",       "male_title",     "female_title"
 "Despotism",        _("%s Khan"),     _("%s Khatan")
 "Fundamentalism",   _("Lama %s"),     _("?female:Lama %s")
}

flag="kalmykia"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="mongol", "russian", "tibetan", "buryat"

cities =
 "Elst",
 "Lagan",
 "Bašnta",
 "Bulğn selän",
 "Ik Buurl",
 "Kötšnr",
 "Oktyabrin",
 "Priyutnin",
 "Sarpin",
 "Tselinnin",
 "Har Ğazrin",
 "Yustan",
 "Yašlt",
 "Yaškul",
 "Bağ Dörvd",
 "Aršan",
 "Ik Tsarŋ",
 "Jaškul",
 "Komsomolsk",
 "Tsağan Amn",
 "Priyutn",
 "Sadovoje",
 "Ulan Hol",
 "Mogata",
 "Hargata",
 "Šeret",
 "Kek Usn",
 "Artezian",
 "Sultan",
 "Svetly Erek",
 "Naryn Huduk",
 "Šin Teg",
 "Haltryn Bor",
 "Adyk",
 "Sarul",
 "Atsan Huduk",
 "Hulhuta",
 "Teegin Gerl",
 "Rassvet",
 "Dolan",
 "Harba",
 "Tatal",
 "Sarpa",
 "Honč Nur",
 "Šaridžin",
 "Hanata",
 "Zurgan",
 "Šarnut",
 "Dogzmakin"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
