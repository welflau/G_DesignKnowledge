# Freeciv(nation) · indonesian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/indonesian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的indonesian定义

## 正文
```ruleset
[nation_indonesian]

translation_domain="freeciv"

name=_("Indonesian")
plural=_("?plural:Indonesians")
groups="Modern", "Asian", "Oceanian", "Core"
legend=_("Indonesia is a large country on the Malay Archipelago with central\
 government on the island of Java. The country has a Muslim majority and is\
 one of the most populous in the world.")

leaders = {
 "name",                        "sex"
 "Sukarno",                     "Male"
 "Suharto",                     "Male"
 "Megawati Sukarnoputri",       "Female"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Monarchy",        _("Sultan %s"),          _("Sultana %s")
 "Fundamentalism",  _("Imam %s"),            _("Imama %s")
}
flag="indonesia"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

; Singapore has very similar flag
conflicts_with="Singaporean", "Majapahit", "Sri Vijaya"
civilwar_nations="Acehnese", "East Timorese", "Moluccan", "Papuan"

cities =
 "Jakarta",
 "Surabaya",
 "Bandung",
 "Medan",
 "Semarang",
 "Palembang",
 "Ujung Pandang",
 "Padang",
 "Malang",
 "Surakarta",
 "Banjarmasin",
 "Yogyakarta",
 "Pontianak",
 "Makasar",
 "Cirebon",
 "Bandar Lampung",
 "Denpasar",
 "Mataram",
 "Tegal",
 "Samarinda",
 "Pekan Baru",
 "Banjarmasin",
 "Manadao",
 "Balikpapan",
 "Jambi",
 "Pacet",
 "Ambon"



```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
