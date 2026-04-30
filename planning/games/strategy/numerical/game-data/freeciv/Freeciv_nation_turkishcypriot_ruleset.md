# Freeciv(nation) · turkishcypriot

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/turkishcypriot.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的turkishcypriot定义

## 正文
```ruleset
[nation_turkishcypriot]

name=_("Turkish Cypriot")
plural=_("?plural:Turkish Cypriots")
groups="Modern", "European"
legend=_("Turks first settled in Cyprus after the Ottomans conquered the\
 island in 1571. Political unrest and ethnic tensions between Turkish and\
 Greek Cypriots led to an invasion by the Turkish military in 1974, followed\
 by the declaration of independence of the Turkish Republic of North Cyprus\
 in 1983. Currently, the only country that recognizes the independence of\
 the TRNC is Turkey.")
leaders = {
 "name",                  "sex"
 "Kıbrıslı Mehmed Kamil", "Male"
 "Fazıl Küçük",           "Male"
 "Nejat Konuk",           "Male"
 "Rauf Denktaş",          "Male"
 "Fatma Ekenoğlu",        "Female"
}
flag="trnc"
flag_alt = "-"
style = "classical"

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Despotism",       _("%s Pasha"),       _("?female:%s Pasha")
 "Fundamentalism",  _("Grand Mufti %s"), _("?female:Grand Mufti %s")
}

init_techs=""
init_buildings=""
init_units=""


civilwar_nations = "cypriot", "turkish"

cities = 
 "Lefkoşa",	;Nicosia
 "Gazimağusa",	;Famagusta
 "Girne",	;Kyrenia
 "Güzelyurt",	;Morphou
 "İskele",	;Trikomo
 "Gönyeli",
 "Lefka",
 "Değirmenlik",
 "Lapta",
 "Alsancak",
 "Çatalköy",
 "Yeni Boğaziçi",
 "Beyarmudu",
 "Haspolat",
 "İnönü",
 "Hamitköy",
 "Ozanköy",
 "Dikmen",
 "Alayköy",
 "Akdoğan",
 "Vadili",
 "Karşiyaka",
 "Dipkarpaz",
 "Paşaköy",
 "Yeni Erenköy",
 "Esentepe",
 "Kalkanlı",
 "Mehmetçik",
 "Tatlisu",
 "Geçitkale",
 "Doğancı",
 "Boğazköy",
 "Aydınköy",
 "Böyükkonuk",
 "Akçay",
 "Çamlibel",
 "Serdarlı",
 "Beylerbey",
 "Gaziveren",
 "Zümrütköy",
 "Cihangir"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
