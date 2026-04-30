# Freeciv(nation) · atlantean

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/atlantean.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的atlantean定义

## 正文
```ruleset
[nation_atlantean]

name=_("Atlantean")
plural=_("?plural:Atlantean")
groups="Imaginary"
legend=_("The mythical continent of Atlantis")

leaders = {
 "name",        "sex"
 "Poseidon",    "Male"
 "Evenor",      "Male"
 "Cleito",      "Female"
 "Plato",       "Male"
 "Timaeus",     "Male"
 "Callum",      "Male"
 "Mneseus",     "Male"
 "Calypso",     "Female"
}

ruler_titles = {
 "government",     "male_title",        "female_title"
 "Anarchy",        _("Usurper %s"),     _("?female:Usurper %s")
 "Monarchy",       _("High King %s"),   _("High Queen %s")
}

flag="atlantis"
flag_alt = "-"
style = "Classical"


init_techs=""
init_buildings=""
init_units=""
civilwar_nations="martian", "antarctican", "guanche"

cities =
 "Atlantipolis",
 "Poseidonium",
 "Antillia",
 "Fortunata",
 "Hyperborea",
 "Brasil",
 "Antarctica",
 "Ultima Thule",
 "Zarahemla",
 "Finis Terrae",
 "Bimini",
 "Azora",
 "California",
 "Neptunia",
 "Ophir",
 "Thera",
 "Madeira",
 "Nazca",
 "Brendania",
 "Baltia",
 "Heliopolis",
 "Ymana",
 "Scania",
 "Lemuria",
 "Bermuda",
 "Bacalao",
 "Aztla",
 "Ferro",
 "Santorini",
 "Tartessus",
 "Satanzes",
 "Cumeni",
 "Pepys",
 "Norombega",
 "Rocabarra",
 "Royllo",
 "Mu",
 "Spartel",
 "Pactacama",
 "Aurora",
 "Arcadia",
 "Lehi Nephi",
 "Albania",
 "Tolla",
 "Mayda",
 "Buyan",
 "Tlila Tlapalla",
 "Australipolis",
 "Estoti",
 "Cassiterus",
 "Cumora",
 "Utopia",
 "Mitla",
 "Calpe",
 "Symplegada",
 "Aeaea",
 "Argyre",
 "Amazonia",
 "Ogygia",
 "Ani Anti",
 "Xibalba",
 "Tlaloca",
 "Sais",
 "Calypsia",
 "Vilcabamba",
 "Gaia",
 "Malta"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
