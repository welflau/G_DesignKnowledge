# Freeciv(nation) · iranian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/iranian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的iranian定义

## 正文
```ruleset
[nation_iranian]

name=_("Iranian")
plural=_("?plural:Iranians")
groups="Modern", "Asian"
legend=_("Iran means \"Land of the Aryans\" - long known as Persia in the\
 Western world. The country is today an Islamic Republic and a major\
 power in the Middle East.")

; Some of the leaders of Iran from 500 years ago to now sorted by date
leaders = {
 "name",                        "sex"
; Islamic Republic
 "Mohammad Khatami",            "Male"
 "Akbar Hashemi Rafsanjani",    "Male"
 "Ruhollah Khomeini",           "Male"
; Pahlavi
 "Reza Pahlavi",                "Male"
 "Mohammad Reza Pahlavi",       "Male"
; Ghajar
 "Agha Mohammad Khan",          "Male"
 "Fathali",                     "Male"
 "Nasereddin",                  "Male"
 "Mozafferreddin",              "Male"
 "Mohammad Ali",                "Male"
; Zand
 "Karim Khan",                  "Male"
 "Lotfali Khan",                "Male"
; Afshar
 "Nader",                       "Male"
 "Shahrokh",                    "Male"
; Safavi
 "Ismail I",                    "Male"
 "Tahmasb I",                   "Male"
 "Abbas I",                     "Male"
}

ruler_titles = {
 "government",      "male_title",          "female_title"
 "Despotism",       _("Leader %s"),        _("?female:Leader %s")
 "Monarchy",        _("%s Shah"),          _("%s Shahbanu")
 "Fundamentalism",  _("Ayatollah %s"),     _("?female:Ayatollah %s")
}

flag="iran"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Persian"
civilwar_nations="Tajik", "Pashtun", "Azeri"

; http://de.wikipedia.org/wiki/Liste_der_Städte_im_Iran
cities =
 "Tehran (mountains, hills, !ocean)",
 "Mashhad",
 "Isfahan (river)",
 "Karaj",
 "Tabriz",
 "Shiraz",
 "Qom (!ocean, desert)",
 "Ahvaz (!ocean, desert)",
 "Kermanshah",
 "Uromia (ocean, river)",
 "Rasht",
 "Kerman",
 "Zahedan",
 "Hamedan (hills)",
 "Arak",
 "Yazd",
 "Ardabil",
 "Abadan",
 "Zanjan",
 "Sanandaj",
 "Qazvin (!ocean)",
 "Khorramshahr",
 "Khorramabad",
 "Islamshahr",
 "Bandar Abbas (ocean, swamp)",
 "Kashan",
 "Khomeinishahr",
 "Ghods",
 "Sari (ocean, swamp)",
 "Borujerd",
 "Gharchak",
 "Gorgan",
 "Sabzevar",
 "Najafabad",
 "Nishapur",
 "Nazarbad",
 "Bukan",
 "Dezful",
 "Sirjan",
 "Babol",
 "Amol",
 "Birjand",
 "Bojnurd",
 "Qaemshahr",
 "Varamin",
 "Malayer",
 "Saveh",
 "Khoy",
 "Maragheh",
 "Andimeshk",
 "Mahabad",
 "Bushehr",
 "Saqqez",
 "Rafsanjan (!ocean, desert)",
 "Shahinshahr",
 "Ilam",
 "Yasuj",
 "Miandoab",
 "Shahrud",
 "Gonbad-e Kavous",
 "Iranshahr",
 "Marvdasht",
 "Shahr-e Kord",
 "Torbat-e Heydarieh",
 "Semnan",
 "Marand",
 "Zabol",
 "Dorud",
 "Quchan",
 "Jiroft",
 "Masjed Soleyman",
 "Marivan",
 "Bandar-e Anzali (ocean, swamp)",
 "Jahrom",
 "Izeh",
 "Baneh",
 "Parsabad",
 "Shahreza",
 "Kuhdasht",
 "Hormuz (ocean, swamp)",
;Islands
 "Kish (ocean, hills)",
 "Gheshm (ocean)",
 "Khark (ocean)"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
